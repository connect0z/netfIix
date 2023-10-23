"use strict";

$(".this_token_checkBox").on("click", function () {
  if ($(".token_input").css("display") == "none") {
    $(".token_input").css("display", "block");
    $(".inp_password").css("width", "100%");
  } else {
    $(".token_input").css("display", "none");
  }
}).trigger("click");
$("input.slimodan_input").on("focus", function () {
  $(this).prev("label").css({
    "left": "0px",
    "top": "-20px"
  });
});