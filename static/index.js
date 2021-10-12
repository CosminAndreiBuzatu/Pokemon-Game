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

function reloadCards(response){
    loadCard(response.name1)
    loadCard2(response.name2)
    loadCardsLeft1()
    loadCardsLeft2()
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

function refreshCards(){
    $("#content").load( "ajax/test.html" );
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
        reloadCards(response)
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
        reloadCards(response)
      },
      error: function(err) {}
  });
}
