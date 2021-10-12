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

function reloadCards() {
  alert("Reload Cards")
  $.ajax({
      url: "/card?player=1",
      type: "get",
      data: { },
      success: function(response) {
        $("#pokemonCard").html(response)
      },
      error: function(err) {}
  });
  $.ajax({
      url: "/card?player=2",
      type: "get",
      data: { },
      success: function(response) {
        $("#pokemonCard2").html(response)
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
      url: "/selectMove",
      type: "get",
      data: { },
      success: function(response) {
        $.getJSON('/userAttacks?attackType='+inputVal,
            function(data) {
              //do nothing
            });
      },
      error: function(err) {}
  });
}

function AiAttacks() {
  $.ajax({
      url: "/selectMove",
      type: "get",
      data: { },
      success: function(response) {
        $.getJSON('/AiAttacks',
            function(data) {
              //do nothing
            });
      },
      error: function(err) {}
  });
}
