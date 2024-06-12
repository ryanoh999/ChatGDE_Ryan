#!/usr/bin/env python
# coding: utf-8

# In[ ]:


question_1 = """Does the GSP document how DAC stakeholders were given opportunities to engage in
the GSP development process? Provide a one word answer to this question using the
following Spectrum: No = Either there is no reference to DACs or no reference to how DACs
were engaged during GSP development. 
Yes= The GSP references DACs and how they were engaged specifically during development."""

question_2 = """Does the GSP document how tribal stakeholders were given opportunities to engage in the GSP
development process? Provide a one word answer to this question using the following
Spectrum: No = Either there is no reference to Tribes, or no reference to tribal engagement opportunities.
Yes = References specific Tribes in the Basin, documents
targeted engagement opportunities for Tribes."""

question_3 = """Does the GSP document how environmental stakeholders were given opportunities to engage
in the GSP development process? Provide a one word answer to this question using the
following Spectrum: No= Either the GSP does not identify environmental stakeholders or document
targeted engagement opportunities for environmental stakeholders. Yes= Identifies
environmental users as stakeholders, includes targeted engagement opportunities for them."""

question_4 = """Does the Stakeholder Communication and Engagement Plan or GSP include outreach to DACs
during GSP implementation? Provide a one word answer to this question using the following
Spectrum: No= The GSP does not include outreach to DACs, or does not identify DACs as stakeholders
Yes=Identifies DACs as stakeholders, includes DAC-specific outreach (beyond informing)."""

question_5 = """Does the Stakeholder Communication and Engagement Plan or GSP include outreach to tribes
during GSP implementation? Provide a one word answer to this question using the following
Spectrum: No= Either does not identify Tribes as a stakeholder,
or does not include outreach specifically for Tribes.
Yes= Identifies Tribes as stakeholders, includes outreach specifically for Tribes."""

question_6 = """Does the Stakeholder Communication and Engagement Plan or GSP include outreach to
environmental stakeholders during GSP implementation? Provide a one word answer to this
question using the following Spectrum: No = Either does not identify environmental users as
stakeholders or does not outline outreach methods to environmental users.
Yes=Identifies environmental stakeholders, includes outreach material for
environmental stakeholders specifically beyond informing"""

question_7 = """Does the GSP include a Stakeholder Communication and Engagement Plan? Provide a one
word answer to this question using the following Spectrum: No= does not include a C&E plan.
Yes= includes a specific section in GSP dedicated to Stakeholder C&E."""

question_8 = """Does the GSP identify each DAC by name and location on a map? Provide a one word answer
to this question using the following Spectrum: No = does not identify DACs by name, does not
identify DAC locations on a map. Somewhat=identifies DAC location on a map or DAC by name
(one or the other, not both). Yes=Identifies DAC location on a map and identifies them by
name(re: DAC name-- in text or map))."""

question_9 = """Are tribal lands identified and mapped in the basin? Provide a one word answer to this question
using the following Spectrum: No = does not identify Tribal lands on a map, or references in the
text. Somewhat=Tribal lands are identified in text but not mapped OR Tribal lands are mapped
but not identified in text. Yes=Tribal lands are identified in text and mapped."""

question_10 = """Does the GSP describe the size of the population in each DAC? Provide a one word answer to
this question using the following Spectrum: No = no reference to DAC population. Somewhat=
Includes a population map and references DAC separately. Yes= DAC population is explicitly
mentioned or mapped."""

question_11 = """Does the GSP map minimum well depth, or depth range, of domestic wells? Provide a one word
answer to this question using the following Spectrum: No= no map and no reference of well
depth, depth range of domestic wells in text; Map of domestic wells (point or density map of
DOMESTIC wells) but no depth details in map or text. Somewhat= no map but range of depths
and reference to number of domestic wells. Yes= map with DOMESTIC depths (density points
or data, either in text or in map)."""

question_12 = """Does the GSP map the density of domestic wells in the basin? Provide a one word answer to
this question using the following Spectrum: No = no map of domestic wells, reference of
domestic well density in text but no map provided, or no reference at all. Yes= density map of
Domestic wells."""

question_13 = """In the Basin Setting (Groundwater Conditions - Water Quality) section of the GSP, are water
quality contaminants or constituents of concern (e.g., Nitrates; Arsenic, Uranium; DBCP;
1,2,3-TCP; Chromium-6; Perchlorate; Particulate Organic Carbon (POC); Brackish water (TDS;
salts)) identified and mapped (distribution or contaminant plumes) within the plan area? In the
explanations, please specify which contaminants or constituents of concern are present in the
basin, and whether (distribution or contaminant plume) maps and trends were provided for
each. Answer Yes = contaminants are identified, mapped, and spatial trends described in the
text. Somewhat contaminants are identified and/or mapped, but not all spatial trends of
contaminants are provided. No = No contaminants are / are not identified and mapped, and no
spatial trends of contaminants are provided."""

question_14 = """Does the GSP identify the water source for DACs? Provide a one word answer to this question
using the following Spectrum: No= Either there is no mention of DACs, or no mention of their water source. 
Yes=Explicit naming of DAC & Source."""

question_15 = """Are gaining and losing reaches adequately assessed spatially and temporally (e.g., groundwater
levels (from proximate wells to streams and sufficient density of wells along streams) compared
with stream elevation; numerical modeling)? If so, please describe the approach used in the
explanation. Provide a one word answer to this question using the following Spectrum: No = no
map and description (no map is automatic no). Somewhat = includes map but data from one
point in time was used OR includes map but no clear description of methodology. Yes = ISW
map and ISWs were delineated using multiple water year types AND description of temporal
variability."""

question_16 = """Are the conclusions of ISWs (e.g., no ISWs, some gaining/losing/disconnected) consistent with
the assessment? Please describe details in the explanation. Provide a one word answer to this
question using the following Spectrum: No = no conclusions due to lack of data OR vague and
contradictory conclusions that do not make sense with the assessment OR concrete
conclusions made off of little to no evidence or data. Somewhat = conclusions lacks some detail
and evidence to support claims. Yes = the conclusions are coherent with the analysis and
available data."""

question_17 = """Are all shallow principal aquifers acknowledged when defining ISW (in the ISW section)?
Provide a one word answer to this question using the following Spectrum: No = Not all principal
aquifers are acknowledged in the ISW section or a related appendix. 
Yes = Adequate data from shallow
aquifer(s) is used in defining ISWs and all principal shallow aquifers are acknowledged in the
ISW section or a related appendix"""

question_18 = """Were data gaps identified in the ISW section? Provide a one word answer using the following
spectrum:
No = Either no data gaps were identified when there is an obvious lack of data, or there is a
vague/confusing description of ISW data gaps Yes = A clear description of where data gaps exist (temporally and spatially)
in the ISW section or the Data Gaps Section following the assessment"""

question_19 = """In the case of data gaps and uncertainty, were streams mapped and described as potential
ISWs in the GSP? Provide a one word answer to this question using the following Spectrum:
Not Applicable = If ISWs are adequately mapped and there is no uncertainty in the ISW
mapping. No = no description or map of potential ISWs. Somewhat = partial inclusion of
potential ISWs OR only a description but no map or vice versa. Yes = all uncertainties and data
gaps are clearly described and mapped temporarily and spatially."""

question_20 = """Is there an inventory, map, or description of fauna (e.g., birds, fish, amphibian) and flora (e.g.,
plants) species or habitat types in the basin's GDEs? Please indicate in the notes if threatened
and endangered species are identified in the GSP. Provide a one word answer to this question
using the following Spectrum: No = no description of flora and fauna in GDEs. Somewhat =
lacking in either maps/description/inventory of flora and/or fauna OR no mention of
endangered/threatened species. Yes = detailed inventory, maps, or description of flora AND
fauna in GDEs. Also, inclusion of any threatened and/or endangered species in the basin."""

question_21 = """Were GDEs in the basin identified (mapped) and described in the GSP using best available data
(e.g., NC dataset, localized VegMap data)? Please describe which data were used in the Notes.
Provide a one word answer to this question using the following Spectrum: No = No map of
GDEs (or wetlands, riparian veg, etc.). Somewhat = Map of NC dataset polygons with NDMI but
no specific GDE maps OR Maps of GDEs but unclear data/methods used OR use of incorrect
data when mapping GDEs. Yes = GSP used NC dataset or a localized vegMap to describe and
map GDEs and included a clear description of methods."""

question_22 = """Was depth-to-groundwater data from the underlying principal aquifer used to verify the NC
dataset? Provide a one word answer using the following spectrum: No = Either there is no
depth-to-groundwater data used or groundwater measurements are used but there
is a lack of detail in the description of depth-to-groundwater data. Also there might be a lack of
information on which aquifer the data is from. Yes = Depth-to-groundwater data is clearly used
to verify the NC dataset and a description of spatial/temporal data is included."""

question_23 = """Did the GSP avoid using any of the following criteria when deciding whether or not to remove
NC dataset polygons from the final GDE map?: 1)Presence of Surface Water, 2)Distance from
agricultural fields, 3)Principal aquifer was not considered main pumping aquifer, 4)groundwater
connection % of time, 5)Other? If so, please specify in the explanation. Provide a one word
answer to this question using the following Spectrum: No = GSP uses one of the above criteria
(or other illogical reason) to remove a potential GDE. Somewhat = Unclear whether or not the
plan used these criteria - more detail on methods used to verify NC datasets is needed, and/or

the plan did not remove GDE but did label it as “unlikely” based on criteria. Yes = the GSP does
not include any of these criteria to remove a NC dataset polygon."""

question_24 = """Were multiple water year types (e.g., wet, average, dry) of groundwater level data used to
characterize groundwater conditions in the GDEs? Provide a one word answer using the
following spectrum: No = 1 year or less of data was used to characterize groundwater conditions
in the GDE or the GSP lacks a description of multi-year groundwater level data
and/or only post-drought or post-SGMA benchmark data is used (after 2015). Yes = A detailed
explanation of the multi-year groundwater data was used and groundwater data from a prior
drought was included."""

question_25 = """Were depth-to-groundwater measurements under GDEs corrected for land surface elevations?
Provide a one word answer using the following spectrum: No = Either depth-to-groundwater
measurements were interpolated from wells or the model uses groundwater
elevations, but does not correct for land surface elevation. Yes = It is stated that groundwater
measurements used to verify GDEs are corrected for land surface elevation."""

question_26 = """Were data gaps identified when mapping GDEs? Provide a one word answer to this question
using the following Spectrum: No = no data gaps identified when there likely should be.
Somewhat = vague description of a lack of data or data gaps mentioned in other sections of
GSP. Yes = clear description of data gaps (spatial and temporal) in text and/or mapped."""

question_27 = """In the case of data gaps and uncertainty, were potential GDEs mapped and described in the
GSP? Provide a one word answer to this question using the following Spectrum: No = potential
GDEs are not mapped or described in plan. Somewhat = vague description of potential GDEs
and/or no map; wrong methods for assuming non-GDEs. Yes = potential GDEs are clearly
acknowledged and mapped."""

question_28 = """Does the GSP include water demands for native vegetation in the historic, current, and
projected water budgets? Provide a one word answer to this question using the following
spectrum: No = There is no mention of evapotranspiration for the water budget
Yes = Riparian Evapotranspiration is separated out in the water budget charts or tables"""

question_29 = """Does the GSP include water demands for managed wetlands in the historic, current, and
projected water budgets? Provide a one word answer using the following spectrum: No = No
line item or description of managed wetlands’ water demands in water budgets even if wetlands
are discussed in other areas of GSP, or managed wetlands are part of the numerical model
or spreadsheet model assumptions, but are not included as a separate line item.
Yes = There is a separate line item for managed wetlands in water budgets."""


# In[ ]:


question_30 = """Does the GSP incorporate climate change into the projected water budget using DWR change
factors or another source? Provide a one word answer using the following spectrum:
No = Either climate change is not incorporated into the projected water budget or sources are not clearly stated
Yes= Climate change is incorporated into the projected water budget and sources are clearly stated."""

question_31 = """Does the GSP consider multiple climate scenarios in the projected water budget? Provide a one
word answer using the following spectrum: No = No more than one climate scenario used. Yes = Multiple
climate scenarios were used (wet / extremely dry) and provided in the projected water budget"""

question_32 = """Does the GSP incorporate climate change into precipitation inputs for the projected water
budget? Provide a one word answer using the following spectrum: No = Precipitation is not
adjusted for climate change in inputs for the projected water budget, or it is adjusted for climate change,
but there is no quantitative evidence. 
Yes = Precipitation is adjusted for climate change for the projected water budget, and there is
quantitative evidence."""

question_33 = """Does the GSP incorporate climate change into evapotranspiration inputs for the projected water
budget? Provide a one word answer using the following spectrum: No = Evapotranspiration is
not adjusted for climate change in projected water budget inputs, or evapotranspiration is adjusted for 
climate change, but there is no quantitative evidence. Yes = Evapotranspiration inputs are adjusted for
climate change either through change factors or other model projections in projected water
budgets."""

question_34 = """Does the GSP incorporate climate change into surface water flow inputs (e.g., imported water,
streamflow) for the projected water budget? Provide a one word answer using the following
spectrum: No = Surface water inputs are not accounted for in projected water budgets, or 
surface water inputs are stated to be adjusted for climate change, but no quantitative evidence is provided
Yes = Surface water flows are adjusted
for climate change (DWR change factors for spreadsheet model, modeled with adjusted precipitation
and ET for numerical model) and if there is imported water, it is adjusted as well."""

question_35 = """Does the GSP incorporate climate change into sea level inputs for the projected water budget?
Provide an answer using the following spectrum: NotApplicable = The county is not located in a
coastal region.
No = The GSP does not mention or apply sea level rise into the projected water budget, or
sea level inputs are stated to be adjusted for climate change, but it is not specified
as to how they are adjusted. Yes = Clear sea level rise projections due to climate change are
incorporated into the projected water budget."""

question_36 = """Does the GSP calculate a sustainable yield based on the projected water budget with climate
change incorporated? Provide a one word answer using the following spectrum: No = A
sustainable yield is not provided or is not calculated based on a projected water budget with
climate change incorporated.
Yes = A sustainable yield is calculated based on a projected water budget with climate change
incorporated."""

question_37 = """Does the GSP analyze direct or indirect impacts on domestic drinking wells when defining
Undesirable Results for 1) Chronic Lowering of Groundwater Levels and 2) Water Quality (See
line 24)? Provide a one word answer using the following spectrum: No = Either there is no mention of the
impact of domestic drinking wells, or it is mentioned, but it is not well analyzed
Yes = There is a clear impact on drinking water users and an explanation of all COCs."""

question_38 = """Does the GSP analyze direct and indirect impacts on DACs when defining Undesirable Results
for 1) Chronic Lowering of Groundwater Levels, and 2) Water Quality (see line 24)? Provide a
one word answer using the following spectrum: No = There is no explicit mention of DACs when
defining undesirable results for Chronic Lowering and Water Quality. Somewhat = There is an
explicit mention of DACs when defining undesirable results for Chronic Lowering and Water
Quality, but it is not well analyzed. Yes = The impacts to DACs are well analyzed and described
when defining undesirable results for Chronic Lowering and Water Quality."""

question_39 = """Does the GSP analyze direct and indirect impacts on Tribes when defining Undesirable Results
for 1) Chronic Lowering of Groundwater Levels, and 2) Water Quality (see line 24)? Provide a
one word answer using the following spectrum: No = There is no explicit mention of Tribes when
defining undesirable results for Chronic Lowering and Water Quality. Somewhat = There is an
explicit mention of Tribes when defining undesirable results for Chronic Lowering and Water
Quality, but it is not well analyzed. Yes = The impacts to Tribes are well analyzed and described
when defining undesirable results for Chronic Lowering and Water Quality."""

question_40 = """Does the GSP analyze direct and indirect impacts on GDEs when defining Undesirable Results
for 1) Chronic Lowering of Groundwater Levels, and 2) Water Quality (see line 24)? Provide a
one word answer using the following spectrum: No = There is no explicit mention of GDEs when
defining undesirable results for Chronic Lowering and Water Quality, or it is mentioned, 
but it is not well analyzed. Yes = The impacts to GDEs are well analyzed and described
when defining undesirable results for Chronic Lowering and Water Quality."""

question_41 = """Does the GSP establish Water Quality minimum thresholds and measurable objectives for the
identified constituents/contaminants identified in the plan area? Provide a one word answer to
this question using the following spectrum: No = There are not minimum thresholds and measurable objectives
for all COCs
Yes = There are minimum thresholds and measurable objectives for all COCs."""

question_42 = """Are Water Quality minimum thresholds based on or within the Maximum Contaminant levels
(MCLs)? Provide a one word answer to this question using the following spectrum: 
No = There are not minimum thresholds and measurable objectives for all COCs.
Yes = There are minimum thresholds and measurable objectives for all COCs."""

question_43 = """Does the GSP evaluate the cumulative or indirect impacts of proposed groundwater elevation
and water quality minimum thresholds on drinking water users (e.g., domestic wells, municipal
water suppliers)? Provide a one word answer to this question using the following spectrum: 
No = There is no mention of the cumulative or indirect impacts of proposed groundwater elevation
and water quality minimum thresholds on drinking water users or there is a vague
mention of the cumulative or indirect impacts of proposed groundwater elevation and water
quality minimum thresholds on drinking water users and only for one Minimum Threshold
section. Yes = There is a mention of the cumulative or indirect impacts of proposed groundwater
elevation and water quality minimum thresholds on drinking water users in both Minimum
Threshold sections and quantitative data is used to justify/describe this."""

question_44 = """Does the GSP evaluate the cumulative or indirect impacts of proposed groundwater elevation
and water quality minimum thresholds on DACs? Provide a one word answer to this question
using the following spectrum: No = There is no mention of the cumulative or indirect impacts of
proposed groundwater elevation and water quality minimum thresholds on DACs or
there is a vague mention of the cumulative or indirect impacts of proposed groundwater
elevation and water quality minimum thresholds on DACs and only for one Minimum Threshold
section. Yes = There is a mention of the cumulative or indirect impacts of proposed groundwater
elevation and water quality minimum thresholds on DACs in both Minimum Threshold sections
and quantitative data is used to justify/describe this."""

question_45 = """Does the GSP evaluate the cumulative or indirect impacts of proposed groundwater elevation
and water quality minimum thresholds on Tribes? Provide a one word answer to this question
using the following spectrum: No = There is no mention of the cumulative or indirect impacts of
proposed groundwater elevation and water quality minimum thresholds on Tribes or there is a vague mention
of the cumulative or indirect impacts of proposed groundwater
elevation and water quality minimum thresholds on Tribes and only for one Minimum Threshold
section. Yes = There is a mention of the cumulative or indirect impacts of proposed groundwater
elevation and water quality minimum thresholds on Tribes in both Minimum Threshold sections
and quantitative data is used to justify/describe this"""

question_46 = """Does the GSP evaluate the cumulative or indirect impacts of proposed minimum thresholds for
groundwater elevations and ISW on GDEs or environmental beneficial users of surface water?
Provide a one word answer to this question using the following spectrum: No = There is no
mention of the cumulative or indirect impacts of proposed groundwater elevation, water quality
minimum thresholds and ISW on GDEs or environmental beneficial users of surface water
or there is a vague mention of the cumulative or indirect impacts of proposed
groundwater elevation, water quality minimum thresholds and ISW on GDEs or environmental
beneficial users of surface water and only for one Minimum Threshold section. Yes = There is a
mention of the cumulative or indirect impacts of proposed groundwater elevation, water quality
minimum thresholds and ISW on GDEs or environmental beneficial users of surface water in
both Minimum Threshold sections and quantitative data is used to justify/describe this."""

question_47 = """Does the GSP consider Drinking Water Users when establishing water quality and groundwater
elevation measurable objectives? Provide a one word answer to this question using the

following spectrum: No = There is no mention of Drinking Water Users or there is a vague mention
of Drinking Water users and only for one MO section. Yes = There is a mention in both MO sections and 
quantitative data is used to justify/describe this."""

question_48 = """Does the GSP consider DACs when establishing water quality and groundwater elevation
measurable objectives? Provide a one word answer to this question using the following
spectrum: No = Either there is no mention of DACs or there is a vague mention and only for one MO
section. Yes = There is a mention of DACs in both MO sections and it is justified and described."""

question_49 = """Does the GSP consider Tribes when establishing water quality, ISW and groundwater elevation
measurable objectives? Provide a one word answer to this question using the following
spectrum: No = Either there is no mention of Tribes or there is a vague mention and only for one MO
section. Yes = There is a mention of Tribes in both MO sections and it is justified and described."""


# In[ ]:


question_50 = """Does the GSP consider GDEs when establishing ISW and groundwater elevation measurable
objectives? Provide a one word answer to this question using the following spectrum: No = There is not a
mention in both Measurable Objectives sections, and it is either not justified or not described.
Yes = There is a mention in both Measurable Objectives sections and it is both justified and described."""

question_51 = """Do the Representative Monitoring Sites (RMS) in the monitoring network adequately represent
water quality conditions around DACs, domestic wells, and Tribes? Provide a one word answer
to this question using the following Spectrum: No = Some Tribes, DACS and domestic wells do not have an RMS
within one mile, or it is unclear whether they have an RMS within one mile.
Yes = RMS are within one mile of all DAC, domestic and tribal
communities within the basin boundary."""

question_52 = """Do the Representative Monitoring Sites (RMS) in the monitoring network adequately represent
shallow groundwater elevations around DACs, domestic wells, and Tribes? Provide a one word answer
to this question using the following Spectrum: No = Some Tribes, DACS and domestic wells do not have an RMS
within one mile, or it is unclear whether they have an RMS within one mile.
Yes = RMS are within one mile of all DAC, domestic and tribal
communities within the basin boundary."""

question_53 = """Does the GSP include a plan to identify and fill shallow monitoring well data gaps around GDEs
and ISWs in the monitoring network? Provide a one word answer using the following spectrum:
No = There is no clear plan in place to identify and fill shallow well data gaps around GDEs and ISWs.
Yes = GSP has a clear plan to fill spatial and/or temporal data
gaps with regards to GDEs and ISWs in monitoring network sections or PMAs."""

question_54 = """Does the GSP include any plans to incorporate GDE-related biological monitoring into the
monitoring network? Provide a one word answer using the following spectrum: No = There is no clear description
of a plan for biological monitoring. 
Yes = Clear plans for biological monitoring are described; Remote sensing; field surveys, etc."""

question_55 = """Does the GSP include any recharge projects with explicit benefits to the environment? Provide a
one word answer using the following spectrum: No = There is either no ongoing recharge project, or there is
an ongoing recharge project with no explicit benefits to the environment
Yes = The GSP is implementing a recharge project with explicit benefits to the environment."""

question_56 = """Does the GSP include any habitat restoration, stream restoration or invasive species removal
projects? Provide a one word answer using the following spectrum: No = There are no habitat restoration,
stream restoration or invasive species removal projects that are currently being implemented;
Yes = A habitat restoration, stream restoration or invasive species removal project is being implemented"""

question_57 = """Does the GSP identify benefits or impacts of identified projects and management actions to key
beneficial users such as GDEs, drinking water users, tribes, DACs? Provide a one word answer
using the following spectrum: No = Beneficial users are not explicitly identified, or
impacts and benefits are not described, or there are no PMAs with benefits to GDEs, drinking water users, tribes and DACs;
Yes = Beneficial users are explicitly identified, impacts and benefits are described, and there are
PMAs with benefits to GDEs, drinking water users, tribes and DACs"""

question_58 = """Does the GSP include any recharge projects with explicit benefits to DACs? Provide a one word
answer using the following spectrum: No = There is not a recharge project
being implemented, or the recharge project being implemented has no explicit benefits to DACS;
Yes = There is a recharge project being implemented with explicit benefits to DACS"""

question_59 = """Does the GSP include a drinking water well mitigation program to prevent the significant and
unreasonable loss of drinking water? Provide a one word answer using the following spectrum:
No = Either there is no well mitigation program, or there is a well mitigation program 
that is not explicitly beneficial for drinking water users and DACs
Yes = There is a well mitigation program for drinking water users and DACs"""

question_60 = """Does the GSP identify potential impacts to water quality from Projects and Management
Actions? Provide a one word answer to this question using the following spectrum: No = The GSP does not
mention explicit benefits that Projects and Management Actions will have for DACs;
Yes = The GSP mentions explicit benefits that Projects and Management Actions will have for DACs"""

question_61 = """Does the GSP have plans to use Open ET to monitor groundwater extractions from agriculture?
Provide a one word answer using the following spectrum: No = The GSP does not have plans to use Open ET to
monitor groundwater extractions from agriculture Yes = Open ET has been identified as a resource that will
be used for monitoring future extractions from agriculture."""

question_62 = """Does the GSP have plans to install meters on wells in the basin? Provide a one word answer
using the following spectrum: No = There are no plans for installing meters on wells in the basin
Yes = The GSP describes plans for installing meters in detail as a planned project."""

question_63 = """Does the GSP have plans to implement supply reduction (e.g., pumping cuts) in the basin?
Provide a one word answer to this question using the following spectrum: No = There are no plans to implement
supply reduction in the basin.
Yes = Planned PMAs of supply reduction are described."""

question_64 = """Does the GSP have plans to implement supply augmentation (e.g., recharge projects,
desalinating brackish groundwater) in the basin to achieve sustainability? Provide a one word
answer using the following spectrum:No = No plans in place for supply augmentation.
Somewhat = Potential projects or evaluations of feasibility to implement supply augmentation
mentioned. Yes = Planned supply augmentation described in detail to achieve sustainability."""

question_65 = """Does the GSP evaluate whether Project and Management Actions close the gap for current and
projected sustainable yield? Provide a one word answer to this question using the following
spectrum: No = No mention of sustainable yield or overdraft, or closing the gap through PMAs.
Somewhat = PMAs are described to close the gap but are future potential projects AND/OR the
given yield estimate is not the projected sustainable yield. Yes = Planned PMAs are identified as
those that close the gap for projected sustainable yield and is demonstrated quantitatively."""

question_66 = """Does the GSP reference / propose any new water markets in the basin? Provide a one word
answer using the following spectrum: No = No new water markets referenced or proposed.
Yes = New water markets are referenced or proposed."""

question_67 = """Does the GSP identify the potential impact of climate change on obtaining/crossing thresholds
for Sustainable Management Criteria (e.g., as a driver of undesirable results or potential reason
for crossing a minimum threshold)? Provide a one word answer using the following spectrum:
No = The GSP does not explicitly identify climate change as a reason for obtaining/crossing thresholds for SMC.
Yes = The GSP explicitly identifies climate change as a reason for obtaining/crossing thresholds for SMC."""

question_68 = """Does the GSP include details on coordination with water quality control programs? Provide a
one word answer to this question using the following spectrum: No = Either their is no mention of the Regional
Water Quality Control Board, or the Regional
Water Quality Control Board is mentioned but coordination is not discussed at all.
Yes = Coordination between the Regional
Water Quality Control Board and the GSA are clearly defined."""

question_69 = """How many PMAs are there (total #, including tiers)?"""

question_70 = """Are the PMAs all planned projects, all proposed projects, or a mix of both? Provide a
one word answer to this question using the following spectrum: No = Not all of the projects are planned.
Yes = All of the projects are planned."""


# In[ ]:


prompts = [question_1, question_2, question_3, question_4, question_5, question_6,
           question_7, question_8, question_9, question_10, question_11, question_12,
           question_13, question_14, question_15, question_16, question_17, question_18,
           question_19, question_20, question_21, question_22, question_23, question_24,
           question_25, question_26, question_27, question_28, question_29, question_30,
           question_31, question_32, question_33, question_34, question_35, question_36,
           question_37, question_38, question_39, question_40, question_41, question_42,
           question_43, question_44, question_45, question_46, question_47, question_48,
           question_49, question_50, question_51, question_52, question_53, question_54,
           question_55, question_56, question_57, question_58, question_59, question_60,
           question_61, question_62, question_63, question_64, question_65, question_66,
           question_67, question_68, question_69, question_70]

