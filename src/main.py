from datetime import date

from docxtpl import DocxTemplate

# Import tables here so when we fork the processes later for multiprocessing, the tables are already loaded
import helpers.data_parsing.table_import  # noqa
import report_input
from helpers.appendix_context import appendix_context
from helpers.part_1.part_2_community_names import community_names_string, single_community_name
from helpers.part_1_context import part_1_context
from helpers.part_2_context import part_2_context
from helpers.part_3_context import part_3_context
import helpers.post_processing as post_processing

template_name = "hart_template.docx"
output_name = "generated_doc.docx"

doc = DocxTemplate(template_name)
focus = report_input.community_csd if report_input.focus_on_csd else report_input.community_cd
context = {
    'current_date': str(date.today()),
    'community_csds': community_names_string(report_input.community_csds),
    'community_cd': single_community_name(report_input.community_cd),
    'community_csd': single_community_name(report_input.community_csd),
    'community': single_community_name(focus),
    'community_cd_csds_list': community_names_string([report_input.community_cd] + report_input.community_csds),
}
print("Generating document...")
context.update(part_1_context(focus, doc))
print("Part 1 done")
context.update(part_2_context(focus, doc))
print("Part 2 done")
context.update(part_3_context(focus, doc))
print("Part 3 done")
context.update(appendix_context(focus, doc))
print("Appendix done")
print("Saving document...")
doc.render(context, autoescape=True)
doc.save(output_name)
print("Saved, now doing post processing...")

# After we use the auto-generated library, we will "manually" change the rows on some tables to be bolded

post_processing.run(output_name)
print("Done")