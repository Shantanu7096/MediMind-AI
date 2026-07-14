function createChart(canvas, label, labels, data, color){

    new Chart(

        document.getElementById(canvas),

        {

            type:'line',

            data:{

                labels:labels,

                datasets:[{

                    label:label,

                    data:data,

                    borderColor:color,

                    backgroundColor:color,

                    fill:false,

                    tension:0.4

                }]

            },

            options:{

                responsive:true,

                maintainAspectRatio:false

            }

        }

    );

}