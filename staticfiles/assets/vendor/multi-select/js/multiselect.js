// jQuery(document).ready(function($) {
//     'use strict';

//     // ============================================================== 
//     // select-1
//     // ============================================================== 
//      if ($("#my-select, #pre-selected-options").length) {
//        $('#my-select, #pre-selected-options').multiSelect()

//     }
  

//     // ============================================================== 
//     // select-2
//     // ============================================================== 
//     if ($("#callbacks").length) {
//        $('#callbacks').multiSelect({
//         afterSelect: function(values) {
//             alert("Select value: " + values);
//         },
//         afterDeselect: function(values) {
//             alert("Deselect value: " + values);
//         }
//     });

//     }
  
  

//     // ============================================================== 
//     // select-3
//     // ============================================================== 
//     if ($("#keep-order").length) {
//      $('#keep-order').multiSelect({ keepOrder: true });

//     }



//     // ============================================================== 
//     // select-4
//     // ============================================================== 
//      if ($("#public-methods").length) {
//       $('#public-methods').multiSelect();
//     $('#select-all').click(function() {
//         $('#public-methods').multiSelect('select_all');
//         return false;
//     });
//     $('#deselect-all').click(function() {
//         $('#public-methods').multiSelect('deselect_all');
//         return false;
//     });
//     $('#select-100').click(function() {
//         $('#public-methods').multiSelect('select', ['elem_0', 'elem_1'..., 'elem_99']);
//         return false;
//     });
//     $('#deselect-100').click(function() {
//         $('#public-methods').multiSelect('deselect', ['elem_0', 'elem_1'..., 'elem_99']);
//         return false;
//     });
//     $('#refresh').on('click', function() {
//         $('#public-methods').multiSelect('refresh');
//         return false;
//     });
//     $('#add-option').on('click', function() {
//         $('#public-methods').multiSelect('addOption', { value: 42, text: 'test 42', index: 0 });
//         return false;
//     });

//     }
    
    
//     // ============================================================== 
//     // select-5
//     // ============================================================== 
// if ($("#optgroup").length) {
//     $('#optgroup').multiSelect({ selectableOptgroup: true });
// }
//     // ============================================================== 
//     //select-6
//     // ============================================================== 
// if ($("#disabled-attribute").length) {

//      $('#disabled-attribute').multiSelect();
//  }
//     // ============================================================== 
//     // select-7
//     // ============================================================== 
// if ($("#custom-headers").length) {
//      $('#custom-headers').multiSelect({
//         selectableHeader: "<div class='custom-header'>Selectable items</div>",
//         selectionHeader: "<div class='custom-header'>Selection items</div>",
//         selectableFooter: "<div class='custom-header'>Selectable footer</div>",
//         selectionFooter: "<div class='custom-header'>Selection footer</div>"
//     });


// }
// });