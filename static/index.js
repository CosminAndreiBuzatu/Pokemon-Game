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
    var element = document.getElementById("pokemonCard2");
    element.style.opacity = inputVal;
}

function reloadCards(response){
    loadCard(response.name1)
    loadCard2(response.name2)
    loadCardsLeft1()
    loadCardsLeft2()
    loadSelectMove()
    if (response.win){
        cardOpacity1("1.0")
        cardOpacity2("0.25")
    }
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
        cardOpacity1("1.0")
        cardOpacity2("1.0")
        setTimeout(function(){reloadCards(response); }, 1000);
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
        cardOpacity2("1.0")
        setTimeout(function(){reloadCards(response); }, 1000);

      },
      error: function(err) {}
  });
}
