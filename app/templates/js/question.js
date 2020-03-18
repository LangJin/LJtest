$(document).ready(function() {
    initialize_page();
    get_tag_list(1);
    get_questions_list(1);
    set_copyright_version();

});

//获取标签列表
function get_tag_list(type){
    $.ajax(
        {
            type:'get',
            url:get_url("/gettaglist?type=" + type),
            success:function(str){//返回json结果
                if (str.status == 200) {
                    var content = "";
                    var data = str.data[0].tags;
                    var tags = data.split(",");
                    for (var i = 0; i < tags.length; i++){
                        var tag = "<div class=\"meaus-item\">"+tags[i]+"</div>";
                        content = content + tag;
                    }
                    $("#meaus").append(content);
                }

            },
            fail: function(err, status) {
                alert("数据获取失败！");
                console.log(err);
        }}
    );
    
}

// 获取问题列表
function get_questions_list(nums) {
    $.ajax({
        type: 'get',
        url: get_url("/getquestions?pagenum=" + nums),
        success: function(str) { //返回json结果
            if (str.status == 200) {
                // 获取成功
                var c = '';
                var content = '';
                var datas = str.data.contentlist
                var counts = str.data.counts
                for (var i = 0; i < datas.length; i++) {
                    var author_id = datas[i].uid;
                    var author_name = datas[i].nickname
                    var author_headpic = get_img_url(datas[i].headpic)
                    var author_infomation = datas[i].userinfo

                    var question_reading = 456; // 阅读量
                    var question_comments = 456; // 评论量
                    var question_likes = datas[i].goods; // 点赞数
                    var question_collectons = datas[i].collections; // 收藏量

                    var question_id = datas[i].id; // 文章id
                    var question_title = datas[i].title; // 标题
                    var question_content = datas[i].brief; // 简介
                    var question_creattime = datas[i].times; // 创建时间
                    var question_imag_url = get_img_url(datas[i].ximg); // 文章图片

                    c = '<div class="question-list-item"  style="cursor:pointer;">' +
                        '<p class="fw title" style="word-break:break-all;">' + question_title + '</p>' +
                        '<div class="user-box" onclick="go_question_details(' + question_id + ')">' +
                        '<div class="img-box">' +
                        '<img src="' + author_headpic + '" onclick="go_personal_center(' + author_id + ')" style="cursor:pointer;">' +
                        '</div>' +
                        '<div class="info">' +
                        '<p class="name" onclick="go_personal_center(' + author_id + ')" style="cursor:pointer;">' + author_name + '</p>' +
                        '<p class="job">' + author_infomation + '</p>' +
                        '</div>' +
                        '</div>' +
                        '<p class="word" style="word-break:break-all;">' + question_content + '</p>' +
                        '<div class="question-list-item-other">' +
                        '<div class="other">' +
                        '<span class="other-item date">' + question_creattime + '</span>' +
                        // '<div class="other-item other-icon">' +
                        // '<span class="glyphicon glyphicon-comment"></span>' +
                        // '<span>评论' + question_comments + '</span>' +
                        // '</div>' +
                        // '<div class="other-item other-icon">' +
                        // '<span class="glyphicon glyphicon-open"></span>' +
                        // '<span>阅读' + question_reading + '</span>' +
                        // '</div>' +
                        '<div class="other-item other-icon">' +
                        '<span class="glyphicon glyphicon-user"></span>' +
                        '<span>收藏' + question_collectons + '</span>' +
                        '</div>' +
                        '<div class="other-item other-icon">' +
                        '<span class="glyphicon glyphicon-heart"></span>' +
                        '<span>点赞' + question_likes + '</span>' +
                        '</div>' +
                        '</div>' +
                        '<div data-id="q' + i + '" class="aplly-btn btn-grey" style="" onclick="show_repeat_div(' + i + ')" ">立即回答</div>' +
                        '</div>' +
                        '<div id="q' + i + '" class="message" style="display: none;">' +
                        '<textarea id="q' + question_id + '" class="message-input" placeholder="回答"></textarea>' +
                        '<div data-id="q' + i + '" class="submit btn-grey" onclick="repeat_question(' + question_id + ')">确认</div>' +
                        '</div>' +
                        '</div>'

                    content = content + c;
                }
                $('#question_list').html(content);

                // 分页相关
                $('#total').val(counts);
                compute_pagenum(nums, "get_questions_list", -10000)

            } else {
                alert("数据获取失败！");
                remove_user_login_status(str.msg)

            }

        },
        fail: function(err, status) {
            alert("数据获取失败！");
            console.log(err);
        }
    });
}


// 是否显示回复框
function show_repeat_div(id) {
    var status = $("#q" + id).css('display');
    if (status == 'none') {
        $("#q" + id).show();
    } else {
        $("#q" + id).hide();
    }
}

// 回复问题
function repeat_question(id) {

    var question_id = id;
    var repeat_content = $("#q" + question_id).val();

    is_need_login();
    is_content_not_null(repeat_content);
    var datas = get_json({ "ctype": 1, "comment": repeat_content, "fid": question_id });
    $.ajax({
        type: 'post',
        url: get_url("/comment/new"),
        headers: get_headers(),
        data: datas,
        xhrFields: { withCredentials: true },
        crossDomain: true,
        success: function(str) { //返回json结果
            if (str.status == 200) {
                // 回复成功
                alert("评论成功")
                go_question_details(question_id)
            } else {
                alert(str.msg);
                remove_user_login_status(str.msg)

            }

        },
        fail: function(err, status) {
            alert(err.data);
            console.log(err);
        }
    });
}