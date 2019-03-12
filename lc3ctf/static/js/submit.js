$("#flag-submission").click(function() {

    var id = $(".task-box").data("task_id");
    var flag = $("#flag-input").val();

    $.ajax({
        url: "/submit/" + id + "/" + btoa(flag)
    }).done(function(data) {

        console.log(data);

        if (data["success"]) {
            $("#flag-input").val($(".lang").data("success"));
            $("#flag-submission").removeClass("btn-primary");
            $("#flag-submission").addClass("btn-success");
            $("#flag-submission").attr('disabled','disabled');
        } else {
            $("#flag-input").val($(".lang").data("failure"));
        }
    });
});