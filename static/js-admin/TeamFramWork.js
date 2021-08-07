function Model_Doublicate(Appent_To_ID, Source) {
    let Append_Id = $("#" + Appent_To_ID + "");
    Append_Id.append(Source);
}

function Delete_Model(Class_Click, Remove_Num, Removed_Name) {
    var delete_num;
    $("." + Class_Click + "").click(function () {
        delete_num = $(this).attr("" + Remove_Num + "");
        $("[" + Removed_Name + "=" + delete_num + "]").remove();
    })
    document.addEventListener("click", () => {
        $("." + Class_Click + "").click(function () {
            delete_num = $(this).attr("" + Remove_Num + "");
            $("[" + Removed_Name + "=" + delete_num + "]").remove();
        })
    })
}

function Image_slider(Image_num, Ul_Slider_ID, Ul_Slide_Location_ID, Slider_Tracker_Active_Class, slide_time) {
    for (let i = 1; i <= Image_num; i++) {
        $("#" + Ul_Slider_ID + "").prepend("<li><div class=\"image-p\" id=\"image-slide-" + i + "\"><div class=\"bg-black\"><div class=\"container h-100 position-relative\"><div class=\"text-justify slide-text-parent col-12\"><p class=\"information-slide-text\" id=\"text-slider-" + i + "\"></p></div></div></div></div></li>");
        $("#" + Ul_Slide_Location_ID + "").prepend("<li id=\"slide-" + i + "\" class=\"slider-counter\"></li>")
        $("#image-slide-" + i + "").css({ "background": "url('" + Image_slide[i - 1].Image_Url + "')" });
        $("#text-slider-" + i + "").text("" + Image_slide[i - 1].Information + "");
    }
    $("#slide-1").addClass("" + Slider_Tracker_Active_Class + "");
    var num = 0;
    var doc_Width = $("#" + Ul_Slider_ID + "").width();
    setInterval(function () {
        if (num >= Image_num) {
            num = 0;
        }
        $(".slider-counter").removeClass("" + Slider_Tracker_Active_Class + "");
        $("#" + Ul_Slider_ID + "").css({ "transition": "all 1s", "left": "" + num * doc_Width + "px" });
        $("#slide-" + (num + 1) + "").addClass("" + Slider_Tracker_Active_Class + "");
        num += 1;
    }, slide_time)
}