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
