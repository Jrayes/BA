CREATE TABLE "ServiceHistory" (
    "id" serial NOT NULL PRIMARY KEY,
    "Cartridge_Name" varchar(20) NOT NULL,
    "In_Service"varchar(60) NOT NULL
);

CREATE TABLE "ProductionHistory" (
    "id" serial NOT NULL PRIMARY KEY,
    "Cartridge_Name" varchar(20) NOT NULL,
    "Designer" varchar(20) NOT NULL,
    "Designed" varchar(20) NOT NULL,
    "Manufacturer" varchar(20) NOT NULL,
    "Produced" varchar(20) NOT NULL,
    "Variants" varchar(20) NOT NULL
);
CREATE TABLE "Specifications" (
    "id" serial NOT NULL PRIMARY KEY,
    "Cartridge_Name" varchar(20) NOT NULL,
    "Parent_case" varchar(20) NOT NULL,
    "Case_type" varchar(20) NOT NULL,
    "Bullet_diameter" varchar(20) NOT NULL,
    "Neck_diameter" varchar(20) NOT NULL,
    "Shoulder_diameter"varchar(20) NOT NULL,
    "Base_diameter"varchar(20) NOT NULL,
    "Rim_diameter"varchar(20) NOT NULL
    "Rim_thickness"varchar(20) NOT NULL,
    "Case_length" varchar(20) NOT NULL,
    "Overall_length" varchar(20) NOT NULL,
    "Case_capacity"varchar(20) NOT NULL,
    "Rifling_twist" varchar(20) NOT NULL,
    "Primer_type" varchar(20) NOT NULL,
    "Maximum_pressure" varchar(20) NOT NULL
);

