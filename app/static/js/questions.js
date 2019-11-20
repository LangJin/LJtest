function questionlist(){
    $.ajax({
        type:"get",
        url:"/getquestions",
        success:function(data){
            for (var i in data){
                $("#questionlist").append("<section class=\"list\"><h2 class=\"mucctitle   \"><a href=\"/getquestions/"+data[i].id+"\" target=\"_blank\">"+data[i].title+"</a> </h2>  <time class=\"tebe \">2018.10.29		 &nbsp;<span class=\"zan\">Hot</span> 　</time><div class=\"zuiyao \"><p>"+data[i].brief+"</p></div></section>");
                console.log(i);
            }
        }
    })
}


questionlist();
