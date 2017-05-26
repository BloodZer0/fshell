/*获取高危函数样本库list*/
function lib_danfunc_list(){
    var page = 1;
    var count = 10;

    $.ajax({
        type: "GET",
        async: true,
        dataType: "json",
        url: "/api/lib/danfunc/list",
        data: {
            "page": page,
            "count": count
        },
        error: function(){
            console.log("/api/lib/danfunc/list/error");
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
                    $("#lib_danfunc").html("");
                    $('<tr><td style="text-align:center;padding-top:30px;font-size:16px" colspan="7">没有查询到事件</td></tr>').appendTo($("#lib_danfunc"));
                }else{
                    $("#lib_danfunc").html("");

                    var html_node = '';
                    for(var i=0; i<data.result.length; i++){
                        var item = data.result[i];
                        var id = item['id'];
                        var func_name = item['func_name'];
                        var web_type = item['web_type'];
                        var risk = item['risk'];
                        var remark = item['remark'];
                        var insert_tm = item['insert_tm'];

                        var node = '<tr class="gradeA">';
                        node += '<td>'+id+'</td>';
                        node += '<td><a href="danfunc_id='+id+'">'+func_name+'</a></td>';
                        node += '<td>'+web_type+'</td>';
                        node += '<td>'+risk+'</td>';
                        node += '<td>'+remark+'</td>';
                        node += '<td>'+insert_tm+'</td>';
                        node += [    
                                    '<td class="actions text-center">',
                                    '<a href="#" class="hidden on-editing save-row"><i class="fa fa-save"></i></a>',
                                    '<a href="#" class="hidden on-editing cancel-row"><i class="fa fa-times"></i></a>',
                                    '<a href="#" class="on-default edit-row"><i class="fa fa-pencil"></i></a>',
                                    '<a href="#" class="on-default remove-row"><i class="fa fa-trash-o"></i></a>',
                                    '</td></tr>'
                                ].join('');
                        html_node += node;
                    }
                    $(html_node).appendTo($("#lib_danfunc"));
                }
            }
        }
    });
}




