
/**
 * Jquery Ajax GET请求
 */
function getbigimg() {
    $.ajax({
        type: "get",
        // dataType: "json",
        url: "/home/getbigimg",
        dataType: "json",
        success: function(data){
            for(var i in data){
                $("#demo ul").append('<li data-target="#demo" data-slide-to="'+i+'" class="'+(i == 0? "active" : "")+'"></li>');
                $("#demo .carousel-inner").append('<div class="carousel-item '+(i == 0? "active" : "")+'"><img src="'+data[i].imgpath+'" style="height:450px;"><div class="info carousel-caption"><h1 class="display-2 font-weight-bold">"'+data[i].title+'"</h1><p>"'+data[i].content+'"</p></div>');    
            }
            
            $("#demo").append('<a class="carousel-control-prev" href="#demo" data-slide="prev"><span class="carousel-control-prev-icon"></span></a><a class="carousel-control-next" href="#demo" data-slide="next"><span class="carousel-control-next-icon"></span></a>');

        }
    });
}



function login(){
    $.ajax(
    {
        type:"post",
        dataType:"json",
        url:"/user/login",
        success:function(data){
            alert(data)
        }
    }
)

}

// 局部刷新的方式
// function login(){
//     $.ajax({
//         type: "get",
//         // dataType: "json",
//         url: "/home/login",
//         dataType: "html",
//         success: function(data){
//             $("html").html("");
//             $("html").append(data);
//         }
//     });
// }



// 修改js时,必须加上此方法和对应的调用方法
// 首先执行init_navbar()
// 然后执行navbar_swipe()
// 把渲染效果放在最前面执行

// 初始化导航条样式 - >透明状态
function init_navbar(){

    // 不透明状态
    if ($(".navbar").offset().top > 300) {
        $(".navbar").addClass("bg-dark"); 
        $(".nav-link").removeClass("text-info"); 
        $("#login").removeClass("text-info"); 
    
    // 透明状态
    }else {
        $(".navbar").removeClass("bg-dark");
        $(".nav-link").addClass("text-info"); 
        $("#login").addClass("text-info"); 
    }  
}

// 滑动改变导航条样式
function navbar_swipe(){
        $(window).scroll(function () {  
            // 不透明状态
            if ($(".navbar").offset().top > 300) {
                $(".navbar").addClass("bg-dark"); 
                $(".nav-link").removeClass("text-info"); 
                $("#login").removeClass("text-info"); 
            
            // 透明状态
            }else {
                $(".navbar").removeClass("bg-dark");
                // $(".nav-link").css("color","FFFFFF");
                $(".nav-link").addClass("text-info"); 
                $("#login").addClass("text-info"); 
            }  
        });
}



$("#login").on("click",()=>{
    window.location = "/login";
})

init_navbar()
navbar_swipe();
getbigimg();
