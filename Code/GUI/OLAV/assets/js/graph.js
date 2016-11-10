 window.onload = function(){ $.get("graphData.php",function(data,status){
    data_count = data.split("\n");
    data_count.pop();
    // alert(data_count);
    for(var i =0; i < data_count.length ; i++)
    {
      if ("clean" == data_count[i].split(";")[0])
      {
        var name = data_count[i].split(";")[1].split(":")[0];
        var value = data_count[i].split(";")[1].split(":")[1];
        if ("i" == name)
        {
          var i1 = parseInt(value);
        }
        else if ("a" == name)
        {
          var a1 = parseInt(value);
        }
        else if("w" == name)
        {
          var w1 = parseInt(value);
        }
        else if ("t" == name)
        {
           var t1 = parseInt(value);
        }
        else if("e" == name)
        {
          var e1 = parseInt(value);
        }

      }
      else 
      {
        var name = data_count[i].split(";")[1].split(":")[0];
        var value = data_count[i].split(";")[1].split(":")[1];
        if ("i" == name)
        {
          i2 = parseInt(value);
        }
        else if ("a" == name)
        {
          a2 = parseInt(value);
        }
        else if("w" == name)
        {
          var w2 = parseInt(value);
        }
        else if ("t"== name)
        {
          var t2 = parseInt(value);
        }
        else if("e" == name)
        {
          var e2 = parseInt(value);
        }

      }
    }

    var chart = new CanvasJS.Chart("chartContainer", {            
      title:{
        text: "Log Comparison between a Successful and Error launch"              
      },

      data: [  //array of dataSeries     
      { //dataSeries - first quarter
   /*** Change type "column" to "bar", "area", "line" or "pie"***/        
       type: "column",
       name: "Success",
       dataPoints: [
       { label: "INFO", y: i1 },
       { label: "AUDIT", y: a1 },
       { label: "WARNING", y: w1},                                    
       { label: "ERROR", y: e1 },
       { label: "TRACE", y: t1}
       ]
     },

     { //dataSeries - second quarter

      type: "column",
      name: "Error",                
      dataPoints: [
      { label: "INFO", y: i2},
      { label: "AUDIT", y: a2 },
      { label: "WARNING", y: w2 },                                    
      { label: "ERROR", y: e2 },
      { label: "TRACE", y: t2 }
      ]
    }
    ]
  });

    chart.render();
  });
}
