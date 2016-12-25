# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2016-12-10
# desc: 基础常规方法封装


from fs_base_cfg import *
from fs_log import *


import hashlib
import csv




def get_guid():
    guid = str(uuid.uuid1())
    return guid


# 递归获取web_dir下面的所有文件名文件及其内容
class SearchFile:
    
    def __init__(self):
        self.smallest = BaseConf.SMALLEST_FILESIZE

    def search_file_path(self, web_dir, regex):
        for root, dirs, files in os.walk(web_dir):
            for file in files:
                filename = os.path.join(root, file)

                if not re.search(regex, filename):
                    continue

                if os.path.getsize(filename) < self.smallest:
                    continue
                    
                try:
                    data = open(root + "/" + file, 'rb').read()
                except:
                    data = False
                    Log.err("Could not read file : %s/%s" % (root, file))
                    
                yield data, filename


# 递归获取web_dir下面的所有文件名文件及其大小
class SearchFile_V2:

    def search_file_path(self, web_dir, regex):
        for root, dirs, files in os.walk(web_dir):
            for file in files:
                filename = os.path.join(root, file)

                if not re.search(regex, filename):
                    continue

                filesize = os.path.getsize(filename)
                
                yield filesize, filename


# 读取本地缓存结果数据，避免上传未改动的数据到server
class GetCacheDb:
    
    def __init__(self):
        self.fileList = []


    def read_cache_db(self, out_file):
        if not os.path.isfile(out_file):
            return False, None

        with open(out_file) as f:
            f_csv = csv.DictReader(f)

        return True, f_csv


    def write_cache_db_tmp(self, out_file_tmp, tests, locater, web_dir, regex):

        csv_rows = list()
        csv_headers = ["filename"]
    
        for filesize, filename in locator.search_file_path(web_dir, regex):
            if filesize == 0: continue

            calc_value = dict()
            for test in tests:
                test_name = test.__class__.__name__
                calc_value[test_name] = test.calculate(filename)
                if len(csv_headers) < len(test) +1:
                    csv_headers.append(test_name)
            
                csv_rows.append(calc_value)
            self.fileList.append(filename)
        
        with open(out_file_tmp) as f:
            f_csv = csv.DictWriter(f, csv_headers)
            f_csv.writeheader()
            f_csv.writerows(csv_rows)
    
        return True, csv_rows, fileList



def rm_file(path, delflag=False):
    if not path: return
    if not os.path.exists(path): return

    if os.path.isfile(path):
        os.unlink(path)
        return

    fileList = os.listdir(path)
    if len(fileList) != 0:
        for fname in fileList:
            filePath = "%s/%s" % (path, fname)
            rm_file(filePath, True)

    if delflag:
        os.rmdir(path)


def cp_file(sfile, dfile):
    bRet = True
    rfp = None;
    wfp = None
    try:
        rfp = open(sfile, "rb")
        wfp = open(dfile, "wb")
        wfp.write(rfp.read())
    except Exception, e:
        Log.err("_cpfile(%s, %s) ERR(%s)" % (sfile, dfile, str(e)))
        bRet = False
    finally:
        if rfp != None: rfp.close()
        if wfp != None: wfp.close()
    return bRet



def compute_md5_file(fileName):
    try:
        md5 = hashlib.md5()
        fp = open(fileName, "rb")

        while True:
            data = fp.read(8192)
            if not data: break
            md5.update(data)

        fp.close()
        sret = md5.hexdigest().upper()
        return sret

    except Exception, e:
        Log.err("fileName(%s) ERR(%s)" % (fileName, str(e)))
        return None




if __name__ == "__main__":

    pass
