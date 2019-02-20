//this file should hold the ajax functions for interaction in form_addon, dont delete
function CreateSwap(data){

    try {
        var data_json = JSON.parse(data)
        var swap_fields=data_json['swap_fields']

        swap_fields.unshift('leg')
        window["hot223"].setDataAtCell(0, 0, 'Receive Leg');
        window["hot223"].setDataAtCell(0, 1, 'Pay Leg');

        // Populate Grid
        window["hot223"].updateSettings({
            rowHeaders: swap_fields,
            rowHeaderWidth: 180,
            cells: function(row, col) {
                var cellMeta = {};

                if (swap_fields[row].includes('start_date')) {
                    cellMeta.type = 'date';
                    cellMeta.dateFormat= 'DD-MMM-YYYY';
                    cellMeta.correctFormat= true;
                    cellMeta.defaultDate= '01/01/2019';


                    return cellMeta;
                }

                if (swap_fields[row].includes('end_date')) {
                    cellMeta.type = 'date';
                    cellMeta.dateFormat= 'DD-MMM-YYYY';
                    cellMeta.correctFormat= true;
                    cellMeta.defaultDate= '01/01/2019';


                    return cellMeta;
                }
                if (swap_fields[row].includes('leg_type')) {
                    cellMeta.type = 'dropdown';

                    cellMeta.source = ['fixed', 'float'];
                    return cellMeta;
                }
                if (swap_fields[row].includes('leg_index')) {
                    cellMeta.type = 'dropdown';

                    cellMeta.source = ['Libor3M'];
                    return cellMeta;
                }

                if (swap_fields[row].includes('adjustment')) {
                    cellMeta.type = 'dropdown';

                    cellMeta.source = ['Adjusted', 'Unadjusted','ModifiedFollowing'];
                    return cellMeta;
                }
                if (swap_fields[row].includes('frequency')) {
                    cellMeta.type = 'dropdown';

                    cellMeta.source = ['Quarterly', 'Semianual','Anual'];
                    return cellMeta;
                }

                if (swap_fields[row].includes('day_count')) {
                    cellMeta.type = 'dropdown';

                    cellMeta.source = ['Thirty360()','Thirty360(Thirty360.BondBasis)','Actual360()'];
                    return cellMeta;
                }
            }
        });




        console.log("CreateSWAP Success")

    }
    catch(err){

    }


}

