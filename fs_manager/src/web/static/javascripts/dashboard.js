/* 获取检测概述charts */
function get_det_charts(){

    $.ajax({
        type: "GET",
        async: true,
        dataType: "json",
        url: "/api/dashboard/charts",
        data: {
        },
        error: function(){
            console.log("/api/dashboard/charts/error");
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
                    $("#webshell_list").html("");
                    $('<span>No data...</span>').appendTo($("#webshell_list"));
                }else{
                    var flotDashSales1Data = data.result.flotDashSales1Data;
                    var flotDashSales2Data = data.result.flotDashSales2Data;
                    var flotDashSales3Data = data.result.flotDashSales3Data;

                    window.flotDashSales1Data;
                    window.flotDashSales2Data;
                    window.flotDashSales3Data;
                }
            }
        }
    });   
}




