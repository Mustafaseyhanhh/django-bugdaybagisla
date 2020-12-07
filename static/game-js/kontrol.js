function sesese(bt_id, bt_value) {
  document.getElementById("button_1").disabled = true;
  document.getElementById("button_2").disabled = true;
  document.getElementById("button_3").disabled = true;
  document.getElementById("button_4").disabled = true;
  document.getElementById(bt_id).className = "btn btn-block bg-gradient-warning btn-lg";
  //console.log(bt_id);
  bt_value = document.getElementById(bt_id).innerHTML;
  //console.log("bt_value : " + bt_value);
  var soruid = document.getElementById('soruid').innerHTML;
  //console.log("??????????????????????????????",soruid);
  var kid = document.getElementById('kid').innerHTML;
  //console.log("**********",kid);
  $.ajax({
    url: "/kontrol",
    data: {
      bt_value,
      soruid: soruid,
      kid:kid
    },
    success: function (data) {
      //console.log(data);
      //console.log(data["sonuc"]);
      //console.log(data["cevap"]);
      //console.log(data["gunluk"]);
      //console.log(data["aylik"]);
      //console.log(data["toplam"]);
      //console.log(data["yeni_soru"]);
      //console.log(data["yeni_soru_id"]);
      //console.log(data["a"]);
      //console.log(data["b"]);
      //console.log(data["c"]);
      //console.log(data["d"]);
      if (data["sonuc"] == "1") {
        //console.log("DOĞRU")
        setTimeout(function () {
          document.getElementById(bt_id).className = "btn btn-block bg-gradient-success btn-lg";
          var kazandi = parseInt(document.getElementById("bugday_sayisi").innerHTML) + 10;
          document.cookie = "bugday_sayisi=" + kazandi;
          document.getElementById("bugday_sayisi").innerHTML = kazandi;
          setTimeout(function () {
            $("#soru_panel").hide(500);
            setTimeout(function () {
              document.getElementById("button_1").disabled = false;
              document.getElementById("button_2").disabled = false;
              document.getElementById("button_3").disabled = false;
              document.getElementById("button_4").disabled = false;
              
              document.getElementById(bt_id).className = "btn btn-block btn-outline-secondary btn-lg"
              document.getElementById("soruid").innerHTML = data["yeni_soru_id"];
              document.getElementById("soru_1").innerHTML = data["yeni_soru"];
              document.getElementById("button_1").innerHTML = data["a"];
              document.getElementById("button_2").innerHTML = data["b"];
              document.getElementById("button_3").innerHTML = data["c"];
              document.getElementById("button_4").innerHTML = data["d"];

            }, 500);
            $("#soru_panel").show(500);
          }, 1000);
        }, 1000);
      } else {
        //console.log("YANLIŞ")
        setTimeout(function () {
          document.getElementById(bt_id).className = "btn btn-block bg-gradient-danger btn-lg";
          if (document.getElementById("button_1").innerHTML == "" + (data["cevap"])) {
            document.getElementById("button_1").className = "btn btn-block bg-gradient-success btn-lg"
          }
          if (document.getElementById("button_2").innerHTML == "" + (data["cevap"])) {
            document.getElementById("button_2").className = "btn btn-block bg-gradient-success btn-lg"
          }
          if (document.getElementById("button_3").innerHTML == "" + (data["cevap"])) {
            document.getElementById("button_3").className = "btn btn-block bg-gradient-success btn-lg"
          }
          if (document.getElementById("button_4").innerHTML == "" + (data["cevap"])) {
            document.getElementById("button_4").className = "btn btn-block bg-gradient-success btn-lg"
          }
          setTimeout(function () {
            $("#soru_panel").hide(500);
            setTimeout(function () {
              document.getElementById("button_1").disabled = false;
              document.getElementById("button_2").disabled = false;
              document.getElementById("button_3").disabled = false;
              document.getElementById("button_4").disabled = false;

              document.getElementById("button_1").className = "btn btn-block btn-outline-secondary btn-lg"
              document.getElementById("button_2").className = "btn btn-block btn-outline-secondary btn-lg"
              document.getElementById("button_3").className = "btn btn-block btn-outline-secondary btn-lg"
              document.getElementById("button_4").className = "btn btn-block btn-outline-secondary btn-lg"
              document.getElementById("soruid").innerHTML = data["yeni_soru_id"];
              document.getElementById("soru_1").innerHTML = data["yeni_soru"];
              document.getElementById("button_1").innerHTML = data["a"];
              document.getElementById("button_2").innerHTML = data["b"];
              document.getElementById("button_3").innerHTML = data["c"];
              document.getElementById("button_4").innerHTML = data["d"];


            }, 500);
            $("#soru_panel").show(500);
          }, 1000);
        }, 1000);
      }
    }
  });


}

function yenile() {}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}