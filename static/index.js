function loadCard(pokemonName) {
  $.ajax({
      url: "/card?name="+pokemonName,
      type: "get",
      data: { },
      success: function(response) {
        $("#pokemonCard").html(response)
      },
      error: function(err) {}
  });
}

function loadCard2(pokemonName) {
  $.ajax({
      url: "/card?name="+pokemonName,
      type: "get",
      data: { },
      success: function(response) {
        $("#pokemonCard2").html(response)
      },
      error: function(err) {}
  });
}

function loadCardsLeft1() {
  $.ajax({
      url: "/cardsLeft?player=0",
      type: "get",
      data: { },
      success: function(response) {
        $("#cardsLeft1").html(response)
      },
      error: function(err) {}
  });
}

function loadCardsLeft2() {
  $.ajax({
      url: "/cardsLeft?player=1",
      type: "get",
      data: { },
      success: function(response) {
        $("#cardsLeft2").html(response)
      },
      error: function(err) {}
  });
}

function cardOpacity1(inputVal){
    var element = document.getElementById("pokemonCard");
    element.style.opacity = inputVal;
}

function cardOpacity2(inputVal){
//    var element = document.getElementById("pokemonCard2");
//    element.style.opacity = inputVal;
    $("#pokemonCard2").fadeTo(500, inputVal)
}

function shakeElement(element){
    setTimeout(function(){
        $(element).effect("shake")
    }, 400);
}

function userAttackAnimation(){
    $("#pokemonCard img:last").effect("shake",{times:1,distance:50,direction:'left'})
}

function AiAttackAnimation(){
    $("#pokemonCard2 img:last").effect("shake",{times:1,distance:50,direction:'right'})
}

function KoedAnimation(element){

    $(element).effect("shake", {times:1,distance:50,direction:'up'} );

}

function userKoed(response){
    if (response.win == true){
        KoedAnimation("pokemonCard img:last")
    }
}

function AiKoed(response){
    if (response.win == true){
        KoedAnimation("pokemonCard2 img:last")
    }
}

function reloadCards(response){
    if (response.win){
        cardOpacity1("1.0")
        cardOpacity2("0.0")
    }
    loadCard(response.name1)
    loadCard2(response.name2)
    loadCardsLeft1()
    loadCardsLeft2()
    loadSelectMove()

}

function loadCardGameDisplay(){
  $.ajax({
      url: "/cardGameDisplay",
      type: "get",
      data: { },
      success: function(response) {
        $("#cardGameDisplay").html(response)
      },
      error: function(err) {}
  });
}

function loadSelectMove() {
  $.ajax({
      url: "/selectMove",
      type: "get",
      data: { },
      success: function(response) {
        $("#selectMove").html(response)
      },
      error: function(err) {}
  });
}

function userAttacks(inputVal) {
  $.ajax({
      url: '/userAttacks?attackType='+inputVal,
      type: "get",
      data: { },
      success: function(response) {
        attackAudio();
        $("#pokemonCard2").fadeTo(500, 1, function(){
            userAttackAnimation();
            setTimeout(function(){
                $("#pokemonCard2 img:last").effect("shake", function(){
                    if (response.win == true){
                        victoryAudio();
                        $("#pokemonCard2 img:last").hide("drop", {direction: "down"}, 1000 , function(){
                            $("#pokemonCard2 img:last").show();
                            $("#pokemonCard2 img:last").css("opacity", "0.0");
                            $("#pokemonCard").fadeTo(500, 0)
                            $("#pokemonCard2").fadeTo(500, 0, function(){
                                $("#pokemonCard2 img:last").css("opacity", "1.0");
                                reloadCards(response);
                            });
                            setTimeout(function(){ $("#pokemonCard").fadeTo(500, 1);}, 500);
                        });
                    } else {
                        reloadCards(response);
                    }
                });
            }, 400);
        });
      },
      error: function(err) {}
  });
}


function AiAttacks() {
  $.ajax({
      url: "/AiAttacks",
      type: "get",
      data: { },
      success: function(response) {
        attackAudio();
        $("#pokemonCard2").fadeTo(500, 1, function(){
            AiAttackAnimation();
            setTimeout(function(){
                $("#pokemonCard img:last").effect("shake", function(){
                    if (response.win == true){
                        KoedAudio();
                        $("#pokemonCard img:last").hide("drop", {direction: "down"}, 1000 , function(){
                            $("#pokemonCard img:last").show();
                            $("#pokemonCard img:last").css("opacity", "0.0");
                            $("#pokemonCard2").fadeTo(500, 0)
                            $("#pokemonCard").fadeTo(500, 0, function(){
                                $("#pokemonCard img:last").css("opacity", "1.0");
                                setTimeout(function(){ $("#pokemonCard").fadeTo(500, 1);}, 500);
                                reloadCards(response);
                            });
                        });
                    } else {
                        reloadCards(response);
                    }
                });
            }, 400);
        });
      },
      error: function(err) {}
  });
}




function attackAudio(){
    var x = document.getElementById("attackAudio");
    setTimeout( function(){x.play();}, 500)
}

function KoedAudio(){
    var x = document.getElementById("KoedAudio");
    x.play();
}
function victoryAudio(){
    var x = document.getElementById("victoryAudio");
    x.play();
}