CREATE TABLE stand_init
(stand_cn varchar(26), stand_id varchar(26), variant varchar(11), inv_year int,
groups text, addfiles text, fvskeywords text, latitude double precision,
longitude double precision, region int, forest int, district int,
compartment int, location int, ecoregion varchar(6), pv_code varchar(10),
pv_ref_code int, age int, aspect double precision, slope double precision,
elevation int, elevft double precision, basal_area_factor double precision,
inv_plot_size double precision, brk_dbh double precision, num_plots int,
nonstk_plots int, sam_w double precision, stk_pcnt double precision,
dg_trans int, dg_measure int, htg_trans int, htg_measure int, mort_measure int,
max_ba double precision, max_sdi double precision, site_species varchar(8),
site_index double precision, model_type int, physio_region int, forest_type int,
state int, county int, fuel_model int, fuel_0_25 double precision,
fuel_25_1 double precision, fuel_0_1 double precision,
fuel_1_3 double precision, fuel_3_6 double precision,
fuel_6_12 double precision, fuel_gt_12 double precision,
fuel_litter double precision, fuel_duff double precision,
photo_ref int, photo_code varchar(13), gis_id int);

COPY stand_init FROM 'C:\\path\\to\\FVS_StandInit.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE tree_init
(stand_id varchar(26), plot_id varchar(26), tree_id int,
tree_count double precision, history int, species varchar(8),
dbh double precision, dg double precision, ht double precision,
htg double precision, httopk double precision, crratio double precision,
damage1 int, severity1 double precision, damage2 int,
severity2 double precision, damage3 int, severity3 double precision,
treevalue int, prescription double precision, age int);

COPY tree_init FROM 'C:\\path\\to\\FVS_TreeInit.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE rotation_age
(stand_id varchar(26), stand_cn varchar(26), fpa_npv int, fsc_npv int,
fpa_msy int, fsc_msy int);

COPY rotation_age FROM 'C:\\path\\to\\RotoAge.csv' DELIMITER ',' CSV HEADER;
