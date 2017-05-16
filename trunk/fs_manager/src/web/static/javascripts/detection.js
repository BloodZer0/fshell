/*获取检测事件list*/
function det_events_list(){
    var last_days = 5;

    $.ajax({
        type: "GET",
        async: true,
        dataType: "json",
        url: "/api/det/events/list",
        data: {
            "last_days": last_days
        },
        error: function(){
            console.log("/api/det/events/list/error");
        },
        success: function(data){
            if(data.code == 101){
                alert(data.message);
            }
            if(data.code == 201){
                var empty = false;
                if (!data.result) {
                    empty = true;
                }
                var dataLen = data.result.length;
                if (dataLen == 0) {
                    empty = true;
                }
                if(empty){
                    $("#time_logs").html("");
                    $('<tr><td style="text-align:center;padding-top:30px;font-size:16px" colspan="7">没有查询到事件</td></tr>').appendTo($("#time_logs"));
                }else{
                    $("#tm-items").html("");

                    var html_node = '';
                    for(var i=0; i<data.result.length; i++){
                        var event = data.result[i];
                        var event_title = event['title'];
                        var event_date = event['date'];
                        var event_lists = event['events'];

                        var res = '';
                        for(var j=0; j < event_lists.length; j++){
                            var event_item = event_lists[j];
                            var file_id = event_item['file_id'];
                            var file_name = event_item['file_name'];
                            var time = event_item['time'];
                            var file_risk = event_item['file_risk'];

                            if(file_risk == 'low'){
                                var file_label = 'primary';
                            }else if(file_risk == 'medium'){
                                var file_label = 'info';
                            }else if(file_risk == 'high'){
                                var file_label = 'warning';
                            }else if(file_risk == 'webshell'){
                                var file_label = 'danger';
                            }else{
                                var file_label = 'default';
                            }

                            res += ' <li><span class="label label-'+file_label+'">'+file_risk+'</span> - <a href="file_info/id='+file_id+'">'+file_name+'</a> '+time+'</li>';
                        }

                        var node = '<li><div class="tm-box"><h4>'+event_title+'</h4> – <span class="release-date">'+event_date+'</span>';
                        node += '<ul class="list-unstyled">'+ res +'</ul></div></li>';
  
                        html_node += node;
                    }
                    $(html_node).appendTo($("#tm-items"));
                }
            }
        }
    });
}


/*获取TOP检测事件-表*/
function det_top_list(){
    var sum_count = 15;
    var weblog_count = 20;
    var statistics_count = 16;
    var fileatt_count = 15;

    $.ajax({
        type: "GET",
        async: true,
        dataType: "json",
        url: "/api/det/top/list",
        data: {
            "sum_count": sum_count,
            "weblog_count": weblog_count,
            "statistics_count": statistics_count,
            "fileatt_count": fileatt_count
        },
        error: function(){
            console.log("/api/det/top/list/error");
        },
        success: function(data){
            if(data.code == 101){
                alert(data.message);
            }
            if(data.code == 201){
                var empty = false;
                if (!data.result) {
                    empty = true;
                }
                var dataLen = data.result.length;
                if (dataLen == 0) {
                    empty = true;
                }
                if(empty){
                    $("#top_list").html("");
                    $('<tr><td style="text-align:center;padding-top:30px;font-size:16px" colspan="7">没有查询到事件</td></tr>').appendTo($("#top_list"));
                }else{

                    /* TOP检测-综合分析 */
                    $("#top_sum").html("");
                    var html_sum = '';
                    var top_sum = data.result.top_sum;
                    for(var i=0; i<top_sum.length; i++){
                        var item = top_sum[i];
                        var file_id = item['file_id'];
                        var file_name = item['filename'];
                        var statics = item['statics'];
                        var fileatt = item['fileatt'];
                        var weblog = item['weblog'];
                        var danfunc = item['danfunc'];
                        var fuzzhash = item['fuzzhash'];
                        var synthetic = item['synthetic'];

                        var top_id = i + 1;
                        var node = '<tr><td>'+top_id+'</td>';
                        node += '<td><a href="file_id='+file_id+'">'+file_name+'</a></td>';
                        node += '<td class="text-right">'+statics+'</td>';
                        node += '<td class="text-right">'+fileatt+'</td>';
                        node += '<td class="text-right">'+weblog+'</td>';
                        node += '<td class="text-right">'+danfunc+'</td>';
                        node += '<td class="text-right">'+fuzzhash+'</td>';
                        node += '<td class="text-right">'+synthetic+'</td></tr>';
                        html_sum += node;
                    }
                    $(html_sum).appendTo($("#top_sum"));


                    /* TOP检测-Web Log分析 */
                    $("#top_weblog").html("");
                    var html_weblog = '';
                    var top_weblog = data.result.top_weblog;
                    for(var i=0; i<top_weblog.length; i++){
                        var item = top_weblog[i];
                        var file_id = item['file_id'];
                        var file_name = item['filename'];
                        var entropy = item['entropy'];
                        var visits = item['visits'];
                        var referer = item['referer'];
                        var keys = item['keys'];
                        var pages = item['pages'];

                        var top_id = i + 1;
                        var node = '<tr><td>'+top_id+'</td>';
                        node += '<td><a href="file_id='+file_id+'">'+file_name+'</a></td>';
                        node += '<td class="text-right">'+entropy+'</td>';
                        node += '<td class="text-right">'+visits+'</td>';
                        node += '<td class="text-right">'+referer+'</td>';
                        node += '<td class="text-right">'+keys+'</td>';
                        node += '<td class="text-right">'+pages+'</td></tr>';
                        html_weblog += node;
                    }
                    $(html_weblog).appendTo($("#top_weblog"));


                    /* TOP检测-统计学分析 */
                    $("#top_statistics").html("");
                    var html_statistics = '';
                    var top_statistics = data.result.top_statistics;
                    for(var i=0; i<top_statistics.length; i++){
                        var item = top_statistics[i];
                        var file_id = item['file_id'];
                        var file_name = item['filename'];
                        var text_ic = item['text_ic'];
                        var text_ent = item['text_ent'];
                        var text_lw = item['text_lw'];
                        var text_cmp = item['text_cmp'];

                        var top_id = i + 1;
                        var node = '<tr><td>'+top_id+'</td>';
                        node += '<td><a href="file_id='+file_id+'">'+file_name+'</a></td>';
                        node += '<td class="text-right">'+text_ic+'</td>';
                        node += '<td class="text-right">'+text_ent+'</td>';
                        node += '<td class="text-right">'+text_lw+'</td>';
                        node += '<td class="text-right">'+text_cmp+'</td></tr>';
                        html_statistics += node;
                    }
                    $(html_statistics).appendTo($("#top_statistics"));


                     /* TOP检测-文本属性分析 */
                    $("#top_fileatt").html("");
                    var html_fileatt = '';
                    var top_fileatt = data.result.top_fileatt;
                    for(var i=0; i<top_fileatt.length; i++){
                        var item = top_fileatt[i];
                        var file_id = item['file_id'];
                        var file_name = item['filename'];
                        var file_ctime = item['file_ctime'];
                        var file_mtime = item['file_mtime'];
                        var file_mode = item['file_mode'];
                        var file_owner = item['file_owner'];

                        var top_id = i + 1;
                        var node = '<tr><td>'+top_id+'</td>';
                        node += '<td><a href="file_id='+file_id+'">'+file_name+'</a></td>';
                        node += '<td class="text-right">'+file_ctime+'</td>';
                        node += '<td class="text-right">'+file_mtime+'</td>';
                        node += '<td class="text-right">'+file_mode+'</td>';
                        node += '<td class="text-right">'+file_owner+'</td></tr>';
                        html_fileatt += node;
                    }
                    $(html_fileatt).appendTo($("#top_fileatt"));
                }
            }
        }
    });
}



