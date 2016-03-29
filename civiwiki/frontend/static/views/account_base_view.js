var interest_views = Backbone.Collection.extend({

    url: '/api/categories',

    parse: function (data) {
        return data.result;
    }

});



var AccountBaseView = Backbone.View.extend({

    el: '#account-base',


    baseTemplate: _.template($('#base-template').html()),
    interestTemplate: _.template($('#interest-tab-template').html()),

    initialize: function (options) {
        var _this = this;
        this.interests = new interest_views();
        options = options || {};
        _this.userModel = options.userModel;
        _this.render();
    },

    render: function () {
        var _this = this;
        _this.$el.empty().append(_this.baseTemplate({
            user: _this.userModel.toJSON()
        }));
        this.getInterests();
        
    },

    getInterests: function(){
                var _this = this;

            this.interests.fetch({ 
            success: function (collection, response) {
                this.interests = collection;

                _this.$el.find('#interests').empty().append(_this.interestTemplate({
                    interest: this.interests.toJSON(),
                    user: _this.userModel.toJSON()

                }));
            }
        });
    },
        events: {
        'click .followInterest': 'editFollowInterest',
    },

    editFollowInterest: function(event){
       var _this = this;
       var tempInterest = JSON.parse(_this.userModel.toJSON().interests);
       var follow = true;
       var unfollow = tempInterest.indexOf(event.target.id);
       var temp1 = event.target.id;
       console.log(temp1);
       var temp = temp1.replace(/ /g,'');
       console.log("Before: " +tempInterest);

       if (unfollow == -1){
            tempInterest.push(event.target.id);
            document.getElementById(event.target.id).innerHTML = "Click Here to Unfollow";
            document.getElementById(temp).innerHTML = "Click Here to Unfollow";
       }else{
            tempInterest.splice(unfollow, 1);
            document.getElementById(event.target.id).innerHTML = "Click Here to Follow";
            document.getElementById(temp).innerHTML = "Click Here to Follow";
       }
       console.log("After: " +tempInterest);
       $.ajax({
            type: 'POST',
            url: 'api/editUser',
            data: {
            user: _this.userModel.toJSON(),
            interests: tempInterest
            },
            success: function (data) {
            },
            error: function(data){
            }
        });

    }


});
