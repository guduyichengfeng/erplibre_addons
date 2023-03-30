odoo.define("aliment.animation", function (require) {
    "use strict";

    let sAnimation = require("website.content.snippets.animation");

    sAnimation.registry.aliment = sAnimation.Class.extend({
        selector: ".o_aliment",

        start: function () {
            let self = this;
            this._eventList = this.$(".aliment_value");
            this._originalContent = this._eventList.text();
            let def = this._rpc({
                route: "/aliment/liste",
            }).then(function (data) {
                if (data.error) {
                    return;
                }

                if (_.isEmpty(data)) {
                    self._eventList.text("No data found");
                    return;
                }


                // self._$loadedContent = $(data);
                // self._eventList.text(data["listes_aliments"]);

                // This will create an unordered list (<ul>) element and append a list item (<li>) element for each item in the data.
                // listes_aliments array. The resulting HTML will be added to the div element with the aliment_value class.
                var list = $("<ul>");
                _.each(data.listes_aliments, function (item) {
                    list.append($("<li>").text(item));
                });
                self._eventList.html(list);
            });
            var ajax = require('web.ajax');

            $('#form').on('submit', function (ev) {
                ev.preventDefault();  // prevent default form submission behavior

                var name = $('#name').val();

                ajax.jsonRpc('/creer', 'call', {
                  'name': name,
                }).then(function (result) {
                  // handle the result of the RPC call here
                  //   console.log(result);
                    location.reload();
                });
            });


            return $.when(this._super.apply(this, arguments), def);
        },
        destroy: function () {
            this._super.apply(this, arguments);
            if (this._$loadedContent) {
                this._eventList.text(this._originalContent);
            }
        },
    });
});
