// textinput.js
    function myFunction() {
                  var text1= $('#text1').val();
                  var text2= $('#text2').val();
                  $.ajax({
                          url: "/join",
                          type: "POST",
                          data: {text1:text1,text2:text2}
                        }).done(function(response) {
                                        var html= " The final RESULT is :  ";
                                        response =response.result;
                                        $.each(response,function(key,val){
                                                              console.log(val);
                                                              html +=val+"<br>"
                                                              // html+="<p>"+val+"<p>"
                                                               });
                                            $(".show-data").append(html);
                                      });
                };
