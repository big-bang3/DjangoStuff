	$(document).ready(function(){
		//document.write(window.location.href);
			$("#name").keyup(function(){

	$.ajax({ url:"http://192.168.137.148:8000/aj_req/",
				 data:{ x:$("#name").val() },
				 dataType:"json",
				 type:"GET",
				 cache:false,
				 success:function(json){ $("#a2").text(json.title);
				 						 $("#a2").attr("class",json.s);
										display_sub();			


				 						},
		});


				
											
			});

		


					$("input").keyup(function(){
							display_sub();
						

												});
					function display_sub(){



							if($("#name").val() && $("#pass1").val() && $("#pass2").val() && $("#a2").attr("class")==1)
   								{	
   									$("#sub").removeAttr('disabled');
   								}
   							else{$("#sub").attr('disabled','disabled');
   									}

					}

	});

	


