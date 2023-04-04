odoo.define("aliment.animation", function (require) {
    "use strict";

    let sAnimation = require("website.content.snippets.animation");
    var ajax = require('web.ajax');
    sAnimation.registry.aliment = sAnimation.Class.extend({
        selector: ".o_aliment",
        read_events: {
            'submit #créer': 'créer',
            'submit #modifier': 'modifier',
        },
        créer: function (ev) {
            ev.preventDefault();  // prevent default form submission behavior

            var name = this.$('#name').val();

            ajax.jsonRpc('/créer', 'call', {
              'name': name,
            }).then(function (result) {
              // handle the result of the RPC call here
              //   console.log(result);
                location.reload();
            });

        },
        modifier: function (ev) {
            ev.preventDefault();  // prevent default form submission behavior

            var name = this.$('#new_name').val(); // get the new name of the aliment
            var id = this.$('#aliment_id').val(); // get the ID of the aliment to be modified

            ajax.jsonRpc('/modifier', 'call', {
                'name': name,
                'aliment_id': id, // pass the ID to the server
            }).then(function (result) {
                // handle the result of the RPC call here
                //   console.log(result);
                location.reload();
            });
        },
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
                
                var list = $("<ul>");
                _.each(data.listes_aliments, function (item) {
                    var listIem = $("<li>");
                    var itemText = "(ID: " + item.id + ") " + item.name;
                    listIem.text(itemText);
                    list.append(listIem);
                });
                self._eventList.html(list);
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

