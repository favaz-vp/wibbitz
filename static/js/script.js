$(document).on("submit", "form.ajax", function (e) {
  e.preventDefault();
  var $this = $(this);

  var url = $this.attr("action");
  var method = $this.attr("method");

  jQuery.ajax({
    type: method,
    url: url,
    dataType: "json",
    data: new FormData(this),
    processData: false,
    contentType: false,
    cache: false,
    success: function (data) {
      var title = data["title"];
      var message = data["message"];
      var status = data["status"];

      console.log(data);

      Swal.fire({
        icon: status,
        title: title,
        text: message,
      });
      if (status == "success") {
        $this.trigger("reset");
      }
    },
    error: function (error) {},
  });
});
