function init() {
				//alert("hi");
				var num;
				var values;
				var table = document.getElementById("outer");

				$.get("flow.php", function(data,status){
						values = data.split("\n");
						values.pop();
						// alert(values);
						num = values[values.length - 1];
						for (var i =0; i <= num -1; i++)
						{
							var row = document.createElement("tr");
							row.id = i+"";
							table.appendChild(row);
						}
						draw(num,200,values, false);
						window.setTimeout(draw2,1000,num,400,values, true,50,0); 
				});
				
			}
			function draw(num,height,values,check) {
				//alert(num);
				//alert("in draw");
				dist = 50;
				for (var i = 0; i <= num-1; i++) {
					var col = document.createElement("td");
					var d = document.createElement("div");
					d.id = "div_"+i+"_"+height;
					d.style.border = "1px solid black";
					//d.style.width = "120px";
					//d.style.height = "50px";
					d.innerHTML = values[i].split(",")[0];
					d.style.backgroundColor = "#E8E8E8";
					if ( check && values[i].split(",")[1] == "True")
					{
						d.style.backgroundColor = "red";
					}
					else if (check && values[i].split(",")[1] == "False")
					{
						d.style.backgroundColor = "green";
					}
					
					// d.style.position = "absolute"; 
					// d.style.position = "absolute";
					// d.style.left = d.offsetLeft+height+"px";
					// d.style.top = d.offsetTop + dist +  "px";
					// dist = dist + 70;

					var outerdiv = document.getElementById("outer");
					// outerdiv.style.position = "relative"
					// outerdiv.appendChild(d);
					col.appendChild(d);
					// alert(document.getElementById(i+""))
					document.getElementById(i+"").appendChild(col);
					
				}


			}
			function draw2(num,height,values,check,dist,i)
			{ 
					var d = document.createElement("div");
					var col = document.createElement("td");
					d.id = "div_"+i;
					d.style.border = "1px solid black";
					//d.style.width = "120px";
					//d.style.height = "50px";
					d.innerHTML = values[i].split(",")[0];
					d.style.backgroundColor = "white";
					if ( check && values[i].split(",")[1] == "True")
					{
						d.style.backgroundColor = "red";
					}
					else if (check && values[i].split(",")[1] == "False")
					{
						d.style.backgroundColor = "green";
					}
					
					// d.style.position = "absolute"; 
					// d.style.position = "absolute";
					// d.style.left = d.offsetLeft+height+"px";
					// d.style.top = d.offsetTop + dist +  "px";
					// dist = dist + 70;

					var outerdiv = document.getElementById("outer");
					// outerdiv.style.position = "relative"
					// outerdiv.appendChild(d);
					col.appendChild(d);
					document.getElementById(i+"").appendChild(col);
					// showDetails()
					i = i + 1;
					var id;
					if(i> num -1)
					{
						window.clearTimeout(id);
						showDetails();
					}
					else
					{
						id = window.setTimeout(draw2,1000,num,height,values,check,dist,i)
					}
				
			} 

			function showDetails()
			{

				var divs = document.getElementsByTagName('div')
				var height = 0;
				for (var i = 0; i < divs.length; i++)
				{
					var outdiv = divs[i];	
					if (divs[i].style.backgroundColor == "red")
					{
						// alert();
						// alert(divs[i].id);
						div_id = divs[i].id;
						divs[i].onclick = details;
						// alert("after click");
					}
				}
			}
				function details(event)
				{

					obj = event.target
					 //alert(event.target);
					var divs = document.getElementsByTagName('div')
					var file = obj.innerHTML
					$.get("errorDetails.php",function(data,status){
							// alert(data);
					arr = data.split("\n");
					for(var j = 0; j < arr.length-1; j++)
					{
								// error = arr[j].split(":")[0];
						var x = arr[j].split(":")[1];
						var y = x.split("=")[1];
								// alert(file+"----"+y);
						if(y == file)
						{	
							var col = document.createElement("td"); 
							// alert(outdiv);
							
							// height = height + 30;
							// disp.style.width = "120px";
							// disp.style.height = "200px";
							//alert("in if");
							// alert(file);
							//alert(arr[j].split(":")[1].split("-")[1])
							error = arr[j].split(":")[0];
							// alert(arr[j]);
							for(var h = 0; h < arr.length-1; h++)
							{
								var disp = document.createElement("div");
								disp.id = "messagediv";
								disp.style.border = "1px solid black";
								// disp.style.border = "1px solid black";
								disp.style.backgroundColor="white";
								if (arr[h].split(":")[0] == error)
								{
									// alert(arr[h]);
									
							// disp.style.border = "1px solid black";
							// disp.style.backgroundColor = "white";
									// disp.style.position = "absolute";
									// disp.style.left = obj.style.offsetLeft+"500px";
									// disp.style.top = obj.style.offsetTop+"px";
									disp.innerHTML=arr[h].split(":")[1];
								}
								// alert(col);
								// alert(disp);
								col.appendChild(disp);
							}
							// alert(obj.id.split("_")[1])
							document.getElementById(obj.id.split("_")[1]).appendChild(col);		
						}
					}
							
						});

					}
			
						