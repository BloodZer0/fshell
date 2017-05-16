
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