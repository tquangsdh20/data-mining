INIT_DBMS = '''
DROP TABLE IF EXISTS "singer" ;
CREATE TABLE "singer" (
    "id"    INTEGER NOT NULL UNIQUE,
    "name"  TEXT NOT NULL,
    PRIMARY KEY("id")
);

DROP TABLE IF EXISTS "song" ;
CREATE TABLE "song" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT NOT NULL,
	"singer_id"	INTEGER NOT NULL,
	"rythm"	TEXT NOT NULL DEFAULT '{}',
	PRIMARY KEY("id"),
	FOREIGN KEY("singer_id") REFERENCES "singer"("id")
);

DROP TABLE IF EXISTS "user" ;
CREATE TABLE "user" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT NOT NULL UNIQUE,
	"playlist"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);

-- INSERT singer TABLE
INSERT INTO "singer" ("id", "name") VALUES ('3', 'Lệ Quyên');
INSERT INTO "singer" ("id", "name") VALUES ('4', 'Lam Trường');
INSERT INTO "singer" ("id", "name") VALUES ('6', 'Bức Tường');
INSERT INTO "singer" ("id", "name") VALUES ('9', 'Hồng Nhung');
INSERT INTO "singer" ("id", "name") VALUES ('17', 'Cẩm Ly');
INSERT INTO "singer" ("id", "name") VALUES ('24', 'Lê Hiếu');
INSERT INTO "singer" ("id", "name") VALUES ('33', 'Hồ Ngọc Hà');
INSERT INTO "singer" ("id", "name") VALUES ('39', 'MTV');
INSERT INTO "singer" ("id", "name") VALUES ('47', 'Đàm Vĩnh Hưng');
INSERT INTO "singer" ("id", "name") VALUES ('49', 'Anh Thơ');
INSERT INTO "singer" ("id", "name") VALUES ('50', 'Mỹ Linh');
INSERT INTO "singer" ("id", "name") VALUES ('54', 'Mỹ Tâm');
INSERT INTO "singer" ("id", "name") VALUES ('55', 'Đan Trường');
INSERT INTO "singer" ("id", "name") VALUES ('74', 'Trần Thu Hà');
INSERT INTO "singer" ("id", "name") VALUES ('79', 'Quang Dũng');
INSERT INTO "singer" ("id", "name") VALUES ('80', 'Tuấn Hưng');
INSERT INTO "singer" ("id", "name") VALUES ('109', 'Quang Hà');
INSERT INTO "singer" ("id", "name") VALUES ('110', 'Phương Thanh');
INSERT INTO "singer" ("id", "name") VALUES ('116', 'Lý Hải');
INSERT INTO "singer" ("id", "name") VALUES ('131', 'Cao Thái Sơn');
INSERT INTO "singer" ("id", "name") VALUES ('159', 'Ngô Thụy Miên');
INSERT INTO "singer" ("id", "name") VALUES ('177', 'Xuân Mai');
INSERT INTO "singer" ("id", "name") VALUES ('207', 'Phan Đinh Tùng');
INSERT INTO "singer" ("id", "name") VALUES ('209', 'Vân Trường');
INSERT INTO "singer" ("id", "name") VALUES ('217', 'Nhiều Ca Sĩ');
INSERT INTO "singer" ("id", "name") VALUES ('227', 'Thu Hà');
INSERT INTO "singer" ("id", "name") VALUES ('273', 'Elvis Phương');
INSERT INTO "singer" ("id", "name") VALUES ('328', 'Đăng Dương');
INSERT INTO "singer" ("id", "name") VALUES ('349', 'Quốc Đại');
INSERT INTO "singer" ("id", "name") VALUES ('354', 'Tóc Tiên');
INSERT INTO "singer" ("id", "name") VALUES ('478', 'Trung Quân');
INSERT INTO "singer" ("id", "name") VALUES ('484', 'Nguyễn Hải Phong');
INSERT INTO "singer" ("id", "name") VALUES ('506', 'Trung Đức');
INSERT INTO "singer" ("id", "name") VALUES ('540', 'Anh Khoa');
INSERT INTO "singer" ("id", "name") VALUES ('767', 'Hà Anh Tuấn');
INSERT INTO "singer" ("id", "name") VALUES ('797', 'Ái Vân');
INSERT INTO "singer" ("id", "name") VALUES ('828', 'Nguyễn Hồng Thuận');
INSERT INTO "singer" ("id", "name") VALUES ('945', 'Toàn Thắng');
INSERT INTO "singer" ("id", "name") VALUES ('1061', 'Lê Thụ');
INSERT INTO "singer" ("id", "name") VALUES ('1064', 'Lê Uyên Phương');
INSERT INTO "singer" ("id", "name") VALUES ('1088', 'Phương Vy');
INSERT INTO "singer" ("id", "name") VALUES ('1136', 'Yến Hương');
INSERT INTO "singer" ("id", "name") VALUES ('1160', 'Thùy Chi');
INSERT INTO "singer" ("id", "name") VALUES ('1262', 'Tố Hà');
INSERT INTO "singer" ("id", "name") VALUES ('1291', 'Đoàn Phi');
INSERT INTO "singer" ("id", "name") VALUES ('1355', 'Wanbi Tuấn Anh');
INSERT INTO "singer" ("id", "name") VALUES ('1382', 'Hamlet Trương');
INSERT INTO "singer" ("id", "name") VALUES ('1384', 'Khánh Phương');
INSERT INTO "singer" ("id", "name") VALUES ('1409', 'Nguyễn Đình Vũ');
INSERT INTO "singer" ("id", "name") VALUES ('1489', 'Bùi Anh Tuấn');
INSERT INTO "singer" ("id", "name") VALUES ('1581', 'Hồ Lệ Thu');
INSERT INTO "singer" ("id", "name") VALUES ('1632', 'Khởi My');
INSERT INTO "singer" ("id", "name") VALUES ('1633', 'Quốc Thiên');
INSERT INTO "singer" ("id", "name") VALUES ('1690', 'Gia Ân');
INSERT INTO "singer" ("id", "name") VALUES ('2380', 'Anh Khang');
INSERT INTO "singer" ("id", "name") VALUES ('2395', 'Akira Phan');
INSERT INTO "singer" ("id", "name") VALUES ('2407', 'The Men');
INSERT INTO "singer" ("id", "name") VALUES ('2428', 'Trường Vũ');
INSERT INTO "singer" ("id", "name") VALUES ('2519', 'Bằng Kiều');
INSERT INTO "singer" ("id", "name") VALUES ('2536', 'Big Bang');
INSERT INTO "singer" ("id", "name") VALUES ('2587', 'Celine Dion');
INSERT INTO "singer" ("id", "name") VALUES ('2639', 'Coldplay');
INSERT INTO "singer" ("id", "name") VALUES ('2715', 'Duy Khánh');
INSERT INTO "singer" ("id", "name") VALUES ('2722', 'Eagles');
INSERT INTO "singer" ("id", "name") VALUES ('2744', 'Eric Clapton');
INSERT INTO "singer" ("id", "name") VALUES ('2773', 'Fiona Fung');
INSERT INTO "singer" ("id", "name") VALUES ('2913', 'James Blunt');
INSERT INTO "singer" ("id", "name") VALUES ('2959', 'Jonas Brothers');
INSERT INTO "singer" ("id", "name") VALUES ('3010', 'Kelly Chen / Trần Tuệ Lâm');
INSERT INTO "singer" ("id", "name") VALUES ('3021', 'Khánh Ly');
INSERT INTO "singer" ("id", "name") VALUES ('3077', 'Lâm Thúy Vân');
INSERT INTO "singer" ("id", "name") VALUES ('3085', 'Lê Uyên');
INSERT INTO "singer" ("id", "name") VALUES ('3117', 'Lenka');
INSERT INTO "singer" ("id", "name") VALUES ('3159', 'Văn Mai Hương');
INSERT INTO "singer" ("id", "name") VALUES ('3174', 'Mariah Carey');
INSERT INTO "singer" ("id", "name") VALUES ('3264', 'Ngọc Lan');
INSERT INTO "singer" ("id", "name") VALUES ('3267', 'Nguyên Khang');
INSERT INTO "singer" ("id", "name") VALUES ('3273', 'Như Quỳnh');
INSERT INTO "singer" ("id", "name") VALUES ('3339', 'Pink');
INSERT INTO "singer" ("id", "name") VALUES ('3443', 'Seventeen');
INSERT INTO "singer" ("id", "name") VALUES ('3541', 'Take That');
INSERT INTO "singer" ("id", "name") VALUES ('3548', 'Taylor Swift');
INSERT INTO "singer" ("id", "name") VALUES ('3570', 'The Beatles');
INSERT INTO "singer" ("id", "name") VALUES ('3672', 'Westlife');
INSERT INTO "singer" ("id", "name") VALUES ('4481', 'Khắc Việt');
INSERT INTO "singer" ("id", "name") VALUES ('4483', 'Hà Linh');
INSERT INTO "singer" ("id", "name") VALUES ('4489', 'M4U Band');
INSERT INTO "singer" ("id", "name") VALUES ('4490', 'Đinh Mạnh Ninh');
INSERT INTO "singer" ("id", "name") VALUES ('4543', 'Miu Lê');
INSERT INTO "singer" ("id", "name") VALUES ('4567', 'Đan Nguyên');
INSERT INTO "singer" ("id", "name") VALUES ('4586', 'Lâm Hùng');
INSERT INTO "singer" ("id", "name") VALUES ('4616', 'Tô Chấn Phong');
INSERT INTO "singer" ("id", "name") VALUES ('4634', 'Tân Nhàn');
INSERT INTO "singer" ("id", "name") VALUES ('4635', 'Thanh Hà');
INSERT INTO "singer" ("id", "name") VALUES ('4837', 'Thái Vũ');
INSERT INTO "singer" ("id", "name") VALUES ('4854', 'Lam Anh');
INSERT INTO "singer" ("id", "name") VALUES ('4887', 'Trung Quân Idol');
INSERT INTO "singer" ("id", "name") VALUES ('4933', 'V.A');
INSERT INTO "singer" ("id", "name") VALUES ('4993', 'Hoàng Dũng');
INSERT INTO "singer" ("id", "name") VALUES ('5100', 'Quốc Anh');
INSERT INTO "singer" ("id", "name") VALUES ('5256', 'Evanescence');
INSERT INTO "singer" ("id", "name") VALUES ('5331', 'Bonnie Tyler');
INSERT INTO "singer" ("id", "name") VALUES ('5523', 'Andy Williams');
INSERT INTO "singer" ("id", "name") VALUES ('5553', 'The Twins');
INSERT INTO "singer" ("id", "name") VALUES ('5727', 'Bread');
INSERT INTO "singer" ("id", "name") VALUES ('5903', 'Adele');
INSERT INTO "singer" ("id", "name") VALUES ('6105', 'Pink Floyd');
INSERT INTO "singer" ("id", "name") VALUES ('6403', 'Tracy Chapman');
INSERT INTO "singer" ("id", "name") VALUES ('6685', 'Michelle');
INSERT INTO "singer" ("id", "name") VALUES ('8181', 'Jeff Buckley');
INSERT INTO "singer" ("id", "name") VALUES ('8195', 'Yanbi');
INSERT INTO "singer" ("id", "name") VALUES ('8201', 'BigDaddy');
INSERT INTO "singer" ("id", "name") VALUES ('8317', 'Paul Anka');
INSERT INTO "singer" ("id", "name") VALUES ('9184', 'Fool''s Garden');
INSERT INTO "singer" ("id", "name") VALUES ('9838', 'Ed Sheeran');
INSERT INTO "singer" ("id", "name") VALUES ('9846', 'Hoài Lâm');
INSERT INTO "singer" ("id", "name") VALUES ('9940', 'M-TP');
INSERT INTO "singer" ("id", "name") VALUES ('10088', 'Binz');
INSERT INTO "singer" ("id", "name") VALUES ('10990', 'Bích Phương Idol');
INSERT INTO "singer" ("id", "name") VALUES ('11979', 'Dương Hoàng Yến');
INSERT INTO "singer" ("id", "name") VALUES ('11998', 'Oringchains');
INSERT INTO "singer" ("id", "name") VALUES ('12444', 'Chí Tài');
INSERT INTO "singer" ("id", "name") VALUES ('12872', 'Quái Vật Tí Hon');
INSERT INTO "singer" ("id", "name") VALUES ('12927', 'Reddy');
INSERT INTO "singer" ("id", "name") VALUES ('12930', 'Connie Kim');
INSERT INTO "singer" ("id", "name") VALUES ('15080', 'Dương Minh Đức');
INSERT INTO "singer" ("id", "name") VALUES ('15426', 'Yoko Takahashi');
INSERT INTO "singer" ("id", "name") VALUES ('15786', 'Ái Phương');
INSERT INTO "singer" ("id", "name") VALUES ('15992', 'Trấn Thành');
INSERT INTO "singer" ("id", "name") VALUES ('15993', 'UVERworld');
INSERT INTO "singer" ("id", "name") VALUES ('16380', 'Rhymastic');
INSERT INTO "singer" ("id", "name") VALUES ('16432', 'Ailee');
INSERT INTO "singer" ("id", "name") VALUES ('16667', 'Ariana Grande');
INSERT INTO "singer" ("id", "name") VALUES ('16669', 'EXID');
INSERT INTO "singer" ("id", "name") VALUES ('17012', 'Lm. JB. Nguyễn Sang');
INSERT INTO "singer" ("id", "name") VALUES ('17141', 'Bảo Linh');
INSERT INTO "singer" ("id", "name") VALUES ('17728', 'B Ray');
INSERT INTO "singer" ("id", "name") VALUES ('17809', 'Kimmese');
INSERT INTO "singer" ("id", "name") VALUES ('18687', 'Kana Hanazawa');
INSERT INTO "singer" ("id", "name") VALUES ('19550', 'Bé Bào Ngư');
INSERT INTO "singer" ("id", "name") VALUES ('19855', 'Hatsune Miku');
INSERT INTO "singer" ("id", "name") VALUES ('20153', 'Hương Tràm');
INSERT INTO "singer" ("id", "name") VALUES ('20196', 'Soobin');
INSERT INTO "singer" ("id", "name") VALUES ('20264', 'Phan Mạnh Quỳnh');
INSERT INTO "singer" ("id", "name") VALUES ('20270', 'Gabrielle Aplin');
INSERT INTO "singer" ("id", "name") VALUES ('20308', 'Trúc Nhân');
INSERT INTO "singer" ("id", "name") VALUES ('20551', 'Only C');
INSERT INTO "singer" ("id", "name") VALUES ('20621', 'Quân Keyboard');
INSERT INTO "singer" ("id", "name") VALUES ('20639', 'Thu Minh');
INSERT INTO "singer" ("id", "name") VALUES ('20693', 'The Carpenters');
INSERT INTO "singer" ("id", "name") VALUES ('20800', 'Ngô Duy Khiêm');
INSERT INTO "singer" ("id", "name") VALUES ('20807', 'Âu Thiên Huy');
INSERT INTO "singer" ("id", "name") VALUES ('20812', 'OneRepublic');
INSERT INTO "singer" ("id", "name") VALUES ('20982', 'Phạm Hồng Phước');
INSERT INTO "singer" ("id", "name") VALUES ('21006', 'Hoàng Yến');
INSERT INTO "singer" ("id", "name") VALUES ('21023', 'Vũ Cát Tường');
INSERT INTO "singer" ("id", "name") VALUES ('21114', 'Kay Trần');
INSERT INTO "singer" ("id", "name") VALUES ('21131', 'Đông Hùng');
INSERT INTO "singer" ("id", "name") VALUES ('21132', 'Min St.319');
INSERT INTO "singer" ("id", "name") VALUES ('21142', 'Karen O');
INSERT INTO "singer" ("id", "name") VALUES ('21184', 'Guns N'' Roses');
INSERT INTO "singer" ("id", "name") VALUES ('21185', 'Sam Smith');
INSERT INTO "singer" ("id", "name") VALUES ('21205', 'Sơn Tùng M-TP');
INSERT INTO "singer" ("id", "name") VALUES ('21241', 'Imagine Dragons');
INSERT INTO "singer" ("id", "name") VALUES ('21245', 'Hari Won');
INSERT INTO "singer" ("id", "name") VALUES ('21282', 'Hòa Minzy');
INSERT INTO "singer" ("id", "name") VALUES ('21306', 'Isaac Thái');
INSERT INTO "singer" ("id", "name") VALUES ('21395', 'Da Lab');
INSERT INTO "singer" ("id", "name") VALUES ('21432', 'JGKid');
INSERT INTO "singer" ("id", "name") VALUES ('21443', 'Megan Trainor');
INSERT INTO "singer" ("id", "name") VALUES ('21467', 'Andiez');
INSERT INTO "singer" ("id", "name") VALUES ('21469', 'Hakoota Dung Hà');
INSERT INTO "singer" ("id", "name") VALUES ('21496', 'Isaac (365 Daband)');
INSERT INTO "singer" ("id", "name") VALUES ('21504', 'Soobin Hoàng Sơn');
INSERT INTO "singer" ("id", "name") VALUES ('21548', 'Cá Hồi Hoang');
INSERT INTO "singer" ("id", "name") VALUES ('21558', 'Đen vâu');
INSERT INTO "singer" ("id", "name") VALUES ('21576', 'Lou Hoàng');
INSERT INTO "singer" ("id", "name") VALUES ('21594', 'Phước Hạnh Nguyễn');
INSERT INTO "singer" ("id", "name") VALUES ('21614', 'Táo');
INSERT INTO "singer" ("id", "name") VALUES ('21627', 'Ngọt.');
INSERT INTO "singer" ("id", "name") VALUES ('21645', 'Phạm Anh Duy');
INSERT INTO "singer" ("id", "name") VALUES ('21666', 'Nguyễn Hoàng Dũng');
INSERT INTO "singer" ("id", "name") VALUES ('21673', 'Mit Tờ Út');
INSERT INTO "singer" ("id", "name") VALUES ('21680', 'Kodaline');
INSERT INTO "singer" ("id", "name") VALUES ('21709', 'Nhạc Thánh Ca');
INSERT INTO "singer" ("id", "name") VALUES ('21731', 'Chi Pu');
INSERT INTO "singer" ("id", "name") VALUES ('21750', 'Issac Thái');
INSERT INTO "singer" ("id", "name") VALUES ('21768', 'Kiều Phạm');
INSERT INTO "singer" ("id", "name") VALUES ('21772', 'Nguyên Jenda');
INSERT INTO "singer" ("id", "name") VALUES ('21775', 'ERIK ST319');
INSERT INTO "singer" ("id", "name") VALUES ('21788', 'Alan Walker');
INSERT INTO "singer" ("id", "name") VALUES ('21806', 'Đức Phúc');
INSERT INTO "singer" ("id", "name") VALUES ('21842', 'Uông Tô Lang');
INSERT INTO "singer" ("id", "name") VALUES ('21925', 'Marzuz');
INSERT INTO "singer" ("id", "name") VALUES ('21937', 'Thành Luke');
INSERT INTO "singer" ("id", "name") VALUES ('21959', 'Camille');
INSERT INTO "singer" ("id", "name") VALUES ('21990', 'Twice');
INSERT INTO "singer" ("id", "name") VALUES ('21996', 'Đinh Tùng Huy');
INSERT INTO "singer" ("id", "name") VALUES ('22000', 'Konamilk');
INSERT INTO "singer" ("id", "name") VALUES ('22008', 'Kiên');
INSERT INTO "singer" ("id", "name") VALUES ('22046', 'Na Anh');
INSERT INTO "singer" ("id", "name") VALUES ('22128', 'Thai Dinh');
INSERT INTO "singer" ("id", "name") VALUES ('22156', 'Huỳnh Tú');
INSERT INTO "singer" ("id", "name") VALUES ('22157', 'Vũ');
INSERT INTO "singer" ("id", "name") VALUES ('22216', 'Plum Village');
INSERT INTO "singer" ("id", "name") VALUES ('22223', 'Vũ Đinh Trọng Thắng');
INSERT INTO "singer" ("id", "name") VALUES ('22231', 'Hải Sâm');
INSERT INTO "singer" ("id", "name") VALUES ('22233', 'Melanie Martinez');
INSERT INTO "singer" ("id", "name") VALUES ('22234', 'Tăng Phúc');
INSERT INTO "singer" ("id", "name") VALUES ('22271', 'Hoàng Phương Trà My');
INSERT INTO "singer" ("id", "name") VALUES ('22281', 'Ban nhạc Ngọt');
INSERT INTO "singer" ("id", "name") VALUES ('22306', 'MONSTAR');
INSERT INTO "singer" ("id", "name") VALUES ('22326', 'N''SYNC');
INSERT INTO "singer" ("id", "name") VALUES ('22333', 'Vũ.');
INSERT INTO "singer" ("id", "name") VALUES ('22346', 'Ba chú bộ đội');
INSERT INTO "singer" ("id", "name") VALUES ('22375', 'Hồ Tiến Đạt');
INSERT INTO "singer" ("id", "name") VALUES ('22395', 'TK From Ling Tosite Sigure');
INSERT INTO "singer" ("id", "name") VALUES ('22401', 'Harry Lu');
INSERT INTO "singer" ("id", "name") VALUES ('22437', 'Lê Thiện Hiếu');
INSERT INTO "singer" ("id", "name") VALUES ('22474', 'Chưa biết');
INSERT INTO "singer" ("id", "name") VALUES ('22504', 'Jang MI');
INSERT INTO "singer" ("id", "name") VALUES ('22520', 'James Arthur');
INSERT INTO "singer" ("id", "name") VALUES ('22530', 'Triết Phạm');
INSERT INTO "singer" ("id", "name") VALUES ('22552', 'Bùi Caroon');
INSERT INTO "singer" ("id", "name") VALUES ('22565', 'Diep Vu Ngoc');
INSERT INTO "singer" ("id", "name") VALUES ('22568', 'Hứa Kim Tuyền');
INSERT INTO "singer" ("id", "name") VALUES ('22583', 'V.Music New');
INSERT INTO "singer" ("id", "name") VALUES ('22620', 'Những Đứa Trẻ');
INSERT INTO "singer" ("id", "name") VALUES ('22698', 'Kha');
INSERT INTO "singer" ("id", "name") VALUES ('22761', 'Rhy');
INSERT INTO "singer" ("id", "name") VALUES ('22830', 'Thế Mạnh');
INSERT INTO "singer" ("id", "name") VALUES ('22849', 'Hy.');
INSERT INTO "singer" ("id", "name") VALUES ('22884', 'Goose House');
INSERT INTO "singer" ("id", "name") VALUES ('22894', 'Ngọc Dolil');
INSERT INTO "singer" ("id", "name") VALUES ('22932', 'Dua Lipa');
INSERT INTO "singer" ("id", "name") VALUES ('22937', 'Bích Phương');
INSERT INTO "singer" ("id", "name") VALUES ('22972', 'Min');
INSERT INTO "singer" ("id", "name") VALUES ('23001', 'Bring Me The Horizon');
INSERT INTO "singer" ("id", "name") VALUES ('23052', 'Harry Styles');
INSERT INTO "singer" ("id", "name") VALUES ('23072', 'Nguyên Hà');
INSERT INTO "singer" ("id", "name") VALUES ('23117', 'Dolphins Band');
INSERT INTO "singer" ("id", "name") VALUES ('23134', 'Long Cao');
INSERT INTO "singer" ("id", "name") VALUES ('23143', 'Long Phạm');
INSERT INTO "singer" ("id", "name") VALUES ('23249', 'Hào GB');
INSERT INTO "singer" ("id", "name") VALUES ('23357', 'Da LAB');
INSERT INTO "singer" ("id", "name") VALUES ('23407', 'R.Tee');
INSERT INTO "singer" ("id", "name") VALUES ('23443', 'Trang Chim Sâu');
INSERT INTO "singer" ("id", "name") VALUES ('23448', 'ERIK');
INSERT INTO "singer" ("id", "name") VALUES ('23492', 'Minh Đinh');
INSERT INTO "singer" ("id", "name") VALUES ('23705', 'Đạt G');
INSERT INTO "singer" ("id", "name") VALUES ('23713', 'Huy');
INSERT INTO "singer" ("id", "name") VALUES ('23751', 'Chester Bennington');
INSERT INTO "singer" ("id", "name") VALUES ('23752', 'Xesi');
INSERT INTO "singer" ("id", "name") VALUES ('23786', 'Lâm Minh Thảo');
INSERT INTO "singer" ("id", "name") VALUES ('24021', 'Tốp ca');
INSERT INTO "singer" ("id", "name") VALUES ('24085', 'Bé Ngọc Ngân');
INSERT INTO "singer" ("id", "name") VALUES ('24497', 'Dương Khải Y');
INSERT INTO "singer" ("id", "name") VALUES ('24588', 'Hyomin (T-ara)');
INSERT INTO "singer" ("id", "name") VALUES ('24624', 'D.I.A');
INSERT INTO "singer" ("id", "name") VALUES ('24833', '$eth');
INSERT INTO "singer" ("id", "name") VALUES ('24880', 'Hugh Jackman');
INSERT INTO "singer" ("id", "name") VALUES ('24885', 'Orange');
INSERT INTO "singer" ("id", "name") VALUES ('25120', 'Red Velvet');
INSERT INTO "singer" ("id", "name") VALUES ('25152', 'La Chi Hào');
INSERT INTO "singer" ("id", "name") VALUES ('25176', 'Vân Dung');
INSERT INTO "singer" ("id", "name") VALUES ('25269', 'K-ICM');
INSERT INTO "singer" ("id", "name") VALUES ('25344', 'Thịnh Suy');
INSERT INTO "singer" ("id", "name") VALUES ('25392', 'Bùi Lan Hương');
INSERT INTO "singer" ("id", "name") VALUES ('25415', 'Lin-Manuel Miranda');
INSERT INTO "singer" ("id", "name") VALUES ('25549', 'Luân Tang (伦桑)');
INSERT INTO "singer" ("id", "name") VALUES ('25599', 'APJ');
INSERT INTO "singer" ("id", "name") VALUES ('25601', 'Freaky');
INSERT INTO "singer" ("id", "name") VALUES ('25689', 'Ngơ ( Hay còn gọi là Long Nger)');
INSERT INTO "singer" ("id", "name") VALUES ('25883', 'Ngọc Duyên');
INSERT INTO "singer" ("id", "name") VALUES ('25915', 'HuyR');
INSERT INTO "singer" ("id", "name") VALUES ('25946', 'BLACKPINK');
INSERT INTO "singer" ("id", "name") VALUES ('26610', 'Đen Vâu');
INSERT INTO "singer" ("id", "name") VALUES ('28036', 'T.R.I');
INSERT INTO "singer" ("id", "name") VALUES ('28494', 'Adeline (Ánh Tuyết)');
INSERT INTO "singer" ("id", "name") VALUES ('28782', 'The Flob');
INSERT INTO "singer" ("id", "name") VALUES ('29240', 'Eric (周興哲)');
INSERT INTO "singer" ("id", "name") VALUES ('29403', '7UPPERCUTS');
INSERT INTO "singer" ("id", "name") VALUES ('33553', 'Thiên Ân');
INSERT INTO "singer" ("id", "name") VALUES ('36083', 'Alec Benjamin');
INSERT INTO "singer" ("id", "name") VALUES ('37717', 'LyLy');
INSERT INTO "singer" ("id", "name") VALUES ('38143', 'Dế Choắt');
INSERT INTO "singer" ("id", "name") VALUES ('38519', 'CHEEZE');
INSERT INTO "singer" ("id", "name") VALUES ('46476', 'Jason Việt Tiến');
INSERT INTO "singer" ("id", "name") VALUES ('47865', 'AMEE');
INSERT INTO "singer" ("id", "name") VALUES ('47974', 'Fugees');
INSERT INTO "singer" ("id", "name") VALUES ('53383', 'Rapper Hải Ninh');
INSERT INTO "singer" ("id", "name") VALUES ('53463', 'Làng Mai');
INSERT INTO "singer" ("id", "name") VALUES ('54705', 'Jeremy Zucker');
INSERT INTO "singer" ("id", "name") VALUES ('56356', 'Yang');
INSERT INTO "singer" ("id", "name") VALUES ('56895', 'Chillies');
INSERT INTO "singer" ("id", "name") VALUES ('58911', 'Những năm 90 band');
INSERT INTO "singer" ("id", "name") VALUES ('58949', 'The90''s Band');
INSERT INTO "singer" ("id", "name") VALUES ('62914', 'TREI');
INSERT INTO "singer" ("id", "name") VALUES ('63407', 'Đình Dũng');
INSERT INTO "singer" ("id", "name") VALUES ('66371', 'TXT');
INSERT INTO "singer" ("id", "name") VALUES ('67941', 'Hương Ly');
INSERT INTO "singer" ("id", "name") VALUES ('70753', 'Khải Nguyễn');
INSERT INTO "singer" ("id", "name") VALUES ('71381', 'Trần Thị Bạch Trà');
INSERT INTO "singer" ("id", "name") VALUES ('71431', 'Gia Bao Nguyen');
INSERT INTO "singer" ("id", "name") VALUES ('72418', 'Minh Mai');
INSERT INTO "singer" ("id", "name") VALUES ('72826', 'Juky San');
INSERT INTO "singer" ("id", "name") VALUES ('72866', 'Ngọt');
INSERT INTO "singer" ("id", "name") VALUES ('73625', 'Antôn Đình Dũng');
INSERT INTO "singer" ("id", "name") VALUES ('75531', 'H2K');
INSERT INTO "singer" ("id", "name") VALUES ('76772', 'Obito');
INSERT INTO "singer" ("id", "name") VALUES ('77259', 'Quân A.P');
INSERT INTO "singer" ("id", "name") VALUES ('81453', 'Yorushika');
INSERT INTO "singer" ("id", "name") VALUES ('82112', 'Minami');
INSERT INTO "singer" ("id", "name") VALUES ('84368', 'Nami Nakagawa');
INSERT INTO "singer" ("id", "name") VALUES ('84493', 'Linked Horizon');
INSERT INTO "singer" ("id", "name") VALUES ('85176', 'Nâu');
INSERT INTO "singer" ("id", "name") VALUES ('89382', 'Asami Seto');
INSERT INTO "singer" ("id", "name") VALUES ('90154', 'Bozitt');
INSERT INTO "singer" ("id", "name") VALUES ('91364', 'Cinnamons');
INSERT INTO "singer" ("id", "name") VALUES ('92418', 'PUBLIC');
INSERT INTO "singer" ("id", "name") VALUES ('93772', 'Carry and Ron');
INSERT INTO "singer" ("id", "name") VALUES ('94003', 'TRUE');
INSERT INTO "singer" ("id", "name") VALUES ('96136', 'Ngọc Kara');
INSERT INTO "singer" ("id", "name") VALUES ('96877', 'YuniBoo');
INSERT INTO "singer" ("id", "name") VALUES ('98212', 'Khả Ngân');
INSERT INTO "singer" ("id", "name") VALUES ('99394', 'Hào');
INSERT INTO "singer" ("id", "name") VALUES ('99524', 'BANNERS');
INSERT INTO "singer" ("id", "name") VALUES ('100125', 'Akari Kito');
INSERT INTO "singer" ("id", "name") VALUES ('100433', 'KALEO');
INSERT INTO "singer" ("id", "name") VALUES ('100807', 'buitruonglinh');
INSERT INTO "singer" ("id", "name") VALUES ('101168', 'DREAMERS');
INSERT INTO "singer" ("id", "name") VALUES ('102117', 'NB3 Hoài Bảo');
INSERT INTO "singer" ("id", "name") VALUES ('102807', 'NamDuc');
INSERT INTO "singer" ("id", "name") VALUES ('103516', 'CHICO with HoneyWorks');
INSERT INTO "singer" ("id", "name") VALUES ('104560', 'Emcee L (Da LAB)');
INSERT INTO "singer" ("id", "name") VALUES ('106570', 'Anh Rồng');
INSERT INTO "singer" ("id", "name") VALUES ('109474', 'Lý Xuân Hoa');
INSERT INTO "singer" ("id", "name") VALUES ('110998', 'Yếu Bất Yếu Mãi Thái');
INSERT INTO "singer" ("id", "name") VALUES ('113471', 'DATKAA');
INSERT INTO "singer" ("id", "name") VALUES ('114167', 'Diệp Tịnh Văn');
INSERT INTO "singer" ("id", "name") VALUES ('116078', 'Tsua Vaj');
INSERT INTO "singer" ("id", "name") VALUES ('123919', 'A Nguyệt Nguyệt (阿YueYue)');
INSERT INTO "singer" ("id", "name") VALUES ('124109', 'Architects');
INSERT INTO "singer" ("id", "name") VALUES ('124375', '4everfreebrony');
INSERT INTO "singer" ("id", "name") VALUES ('125201', 'Thiên Tú');
INSERT INTO "singer" ("id", "name") VALUES ('129997', 'Iruka');
INSERT INTO "singer" ("id", "name") VALUES ('130543', 'nomico');
INSERT INTO "singer" ("id", "name") VALUES ('130814', 'N.Pov Neeb Yaj');
INSERT INTO "singer" ("id", "name") VALUES ('132346', 'Minami (美波)');
INSERT INTO "singer" ("id", "name") VALUES ('137693', 'Quinn');
INSERT INTO "singer" ("id", "name") VALUES ('138272', 'Satoru Hiraide');
INSERT INTO "singer" ("id", "name") VALUES ('140198', 'N/A');
INSERT INTO "singer" ("id", "name") VALUES ('141474', 'PHÚC XP');
INSERT INTO "singer" ("id", "name") VALUES ('143909', '안동영');
INSERT INTO "singer" ("id", "name") VALUES ('143983', '강요셉');
INSERT INTO "singer" ("id", "name") VALUES ('146015', 'RPT MCK');
INSERT INTO "singer" ("id", "name") VALUES ('149907', 'Hoàng Lộc');
INSERT INTO "singer" ("id", "name") VALUES ('152112', 'Christone “Kingfish” Ingram');
INSERT INTO "singer" ("id", "name") VALUES ('156965', 'The Longest Johns');
INSERT INTO "singer" ("id", "name") VALUES ('157445', 'Changg');
INSERT INTO "singer" ("id", "name") VALUES ('157728', 'Sinh hoạt TNTT');
INSERT INTO "singer" ("id", "name") VALUES ('166101', 'Phát Hồ X2X');
INSERT INTO "singer" ("id", "name") VALUES ('166139', 'Truzg');
INSERT INTO "singer" ("id", "name") VALUES ('167135', 'Tan Tran');
INSERT INTO "singer" ("id", "name") VALUES ('169790', 'Zolek');
INSERT INTO "singer" ("id", "name") VALUES ('170756', 'Quách Đỉnh (郭顶)');
INSERT INTO "singer" ("id", "name") VALUES ('171965', 'Bella Poarch');
INSERT INTO "singer" ("id", "name") VALUES ('172639', 'Jinnie');
INSERT INTO "singer" ("id", "name") VALUES ('174068', 'Dhruv');
INSERT INTO "singer" ("id", "name") VALUES ('180532', 'Hà Yumi');
INSERT INTO "singer" ("id", "name") VALUES ('181955', 'Ben Platt');
INSERT INTO "singer" ("id", "name") VALUES ('187825', 'Chalili');
INSERT INTO "singer" ("id", "name") VALUES ('190028', 'Thiện Y Thuần (单依纯)');
INSERT INTO "singer" ("id", "name") VALUES ('190253', 'Đại Huyền (大泫)');
INSERT INTO "singer" ("id", "name") VALUES ('190272', 'TAP');
INSERT INTO "singer" ("id", "name") VALUES ('190931', 'Bạch Lộc (白鹿)');
INSERT INTO "singer" ("id", "name") VALUES ('191171', 'The Sounders');
INSERT INTO "singer" ("id", "name") VALUES ('193278', 'Choi Yu Ree (최유리)');
INSERT INTO "singer" ("id", "name") VALUES ('193675', 'Car the Garden');
INSERT INTO "singer" ("id", "name") VALUES ('193690', 'Kim Jae Hwan (김재환)');
INSERT INTO "singer" ("id", "name") VALUES ('193806', 'Sandeul (산들)');
INSERT INTO "singer" ("id", "name") VALUES ('194470', 'Seung Min (Stray Kids)');

--INSERT users TABLE

INSERT INTO "user" ("name", "playlist") VALUES ('vokaanhduy', '20712 31077 8820 6976 12000 8346 10934 3108 2465 9026 ');
INSERT INTO "user" ("name", "playlist") VALUES ('laithanhhachau', '23026 9722 20712 ');
INSERT INTO "user" ("name", "playlist") VALUES ('dungnguyen27041996', '36580 15383 21932 20712 21212 21430 ');
INSERT INTO "user" ("name", "playlist") VALUES ('PMguitar', '29363 3205 3477 7713 ');
INSERT INTO "user" ("name", "playlist") VALUES ('ndn1999', '44900 36225 9078 43463 99 223 15720 7825 12208 5214 ');
INSERT INTO "user" ("name", "playlist") VALUES ('Quan2401', '2926 33016 34671 32104 31265 30526 30354 11124 10416 6313 ');
INSERT INTO "user" ("name", "playlist") VALUES ('Hasane', '26557 26646 28497 29337 29361 29673 30135 30138 31300 31984 ');
INSERT INTO "user" ("name", "playlist") VALUES ('phanlann299', '5745 17090 14752 7178 20742 8208 40968 19357 31150 11173 ');
INSERT INTO "user" ("name", "playlist") VALUES ('chevan', '941 4302 40778 3758 34392 30099 29119 7275 2700 31620 ');
INSERT INTO "user" ("name", "playlist") VALUES ('huykilo06', '42513 500 37133 39070 15333 7055 28748 12227 1175 35717 ');
INSERT INTO "user" ("name", "playlist") VALUES ('robomai267', '32654 26512 27025 ');
INSERT INTO "user" ("name", "playlist") VALUES ('MellowSkypiea', '');
INSERT INTO "user" ("name", "playlist") VALUES ('bigc1005', '');
INSERT INTO "user" ("name", "playlist") VALUES ('khanhjaki2020', '6428 25711 8573 14282 4674 8644 24803 23426 2867 6821 ');
INSERT INTO "user" ("name", "playlist") VALUES ('nguyenhoa851987', '12031 143 290 1395 1966 33623 7655 18077 29026 28626 ');
INSERT INTO "user" ("name", "playlist") VALUES ('mrmeongao1997', '31015 6338 8067 23107 28500 28498 29134 29146 29149 29148 ');
INSERT INTO "user" ("name", "playlist") VALUES ('teenteenhey', '40498 17782 40968 3126 46320 6583 3716 10279 29397 25956 ');
INSERT INTO "user" ("name", "playlist") VALUES ('Minhbee2811', '49008 38099 22468 38195 1176 37396 37576 37655 37862 42170 ');
INSERT INTO "user" ("name", "playlist") VALUES ('twaynelul1359', '4126 19670 26984 26985 515 13039 32298 31908 14838 16492 ');
INSERT INTO "user" ("name", "playlist") VALUES ('NoNguyen711', '2803 5461 201 2641 20204 3635 3760 6126 12471 1242 ');
INSERT INTO "user" ("name", "playlist") VALUES ('tqml2013', '23065 ');
INSERT INTO "user" ("name", "playlist") VALUES ('nguyenduyphuc102', '8909 6976 26261 5809 26340 26399 462 ');
INSERT INTO "user" ("name", "playlist") VALUES ('lechuong', '');
INSERT INTO "user" ("name", "playlist") VALUES ('oewillrocku', '48406 48326 47063 30491 43732 45336 6977 24024 11 2814 ');
INSERT INTO "user" ("name", "playlist") VALUES ('ThuPham123456789', '');
INSERT INTO "user" ("name", "playlist") VALUES ('trannhutkhoa140201', '43867 47388 16872 195 428 7156 37856 16219 5605 694 ');
INSERT INTO "user" ("name", "playlist") VALUES ('tieuquai', '31828 6751 43745 48827 48991 37133 5321 23 8801 9221 ');
INSERT INTO "user" ("name", "playlist") VALUES ('phunguyen4869', '20 2947 28924 2894 427 24411 8515 24358 8503 8428 ');
INSERT INTO "user" ("name", "playlist") VALUES ('-TurtlyMusic-', '32042 32000 21241 21954 10841 31925 31934 31938 31962 31968 ');
INSERT INTO "user" ("name", "playlist") VALUES ('remmiewemmie', '48530 43834 44782 269 36497 8564 1223 2720 754 772 ');
INSERT INTO "user" ("name", "playlist") VALUES ('thaophuong5312', '');
INSERT INTO "user" ("name", "playlist") VALUES ('pacaroni54321', '31327 31345 31370 31527 31536 31561 31619 39646 39689 39863 ');
INSERT INTO "user" ("name", "playlist") VALUES ('Zon', '17041 16566 8503 13179 13353 15391 15471 16007 15934 17699 ');
INSERT INTO "user" ("name", "playlist") VALUES ('KeySoulTime', '4582 7347 23990 636 2311 8105 29705 39883 5148 25805 ');
INSERT INTO "user" ("name", "playlist") VALUES ('marin3322', '8690 12035 11849 328 6294 14293 10238 17141 7422 42609 ');
INSERT INTO "user" ("name", "playlist") VALUES ('xtnhan', '33591 31782 28437 13490 14820 34083 21286 20508 18438 17463 ');
INSERT INTO "user" ("name", "playlist") VALUES ('NhiTg', '50021 49863 49892 49862 49831 49830 49829 49204 49054 49055 ');
INSERT INTO "user" ("name", "playlist") VALUES ('thaohien3730', '');
INSERT INTO "user" ("name", "playlist") VALUES ('Nguyen_Quoc_Viet', '13548 13729 44316 43777 42774 40323 39452 39451 5844 39240 ');
INSERT INTO "user" ("name", "playlist") VALUES ('trantritan', '');
INSERT INTO "user" ("name", "playlist") VALUES ('Hongtham091124', '39352 35127 26541 6484 33016 33978 33979 33980 33981 33982 ');
INSERT INTO "user" ("name", "playlist") VALUES ('roy', '7307 34936 33094 32641 19008 8671 24356 32574 15918 22470 ');
INSERT INTO "user" ("name", "playlist") VALUES ('haianhkymao99', '13418 13471 17125 35084 33549 13511 13548 13525 23551 22463 ');
INSERT INTO "user" ("name", "playlist") VALUES ('nqd0409', '33117 308 803 26335 5791 7681 19936 12631 ');
INSERT INTO "user" ("name", "playlist") VALUES ('tiendat170197', '');
INSERT INTO "user" ("name", "playlist") VALUES ('trankhanhhung3605', '40700 37537 38360 3760 30537 730 17149 21308 39812 20742 ');
INSERT INTO "user" ("name", "playlist") VALUES ('Riz', '');
INSERT INTO "user" ("name", "playlist") VALUES ('SamuelPan', '');
INSERT INTO "user" ("name", "playlist") VALUES ('Peanutbutter', '538 1126 26036 7815 774 10932 18044 840 36576 35014 ');
INSERT INTO "user" ("name", "playlist") VALUES ('Ngd1305', '8028 2507 529 23991 1244 6218 909 2029 1942 7025 ');
INSERT INTO "user" ("name", "playlist") VALUES ('BonTND', '36109 ');
INSERT INTO "user" ("name", "playlist") VALUES ('cp2001', '29026 ');
INSERT INTO "user" ("name", "playlist") VALUES ('khavi_clover', '19357 10846 10364 134 44836 21815 44063 40728 37133 903 ');
INSERT INTO "user" ("name", "playlist") VALUES ('Peter_Anderson', '36518 36204 36130 31370 35983 36030 31327 35915 31175 31561 ');
INSERT INTO "user" ("name", "playlist") VALUES ('uyenthu', '15804 7055 2195 2881 3673 475 126 3406 40232 3902 ');
INSERT INTO "user" ("name", "playlist") VALUES ('nchuong906', '29687 36561 1244 30568 30537 30540 2452 10089 9195 24001 ');
INSERT INTO "user" ("name", "playlist") VALUES ('hankk201', '30615 16304 25481 ');
INSERT INTO "user" ("name", "playlist") VALUES ('scorpion10mk', '37318 38460 38262 38215 38182 28135 36971 37090 31141 8889 ');
INSERT INTO "user" ("name", "playlist") VALUES ('ssteam', '');
INSERT INTO "user" ("name", "playlist") VALUES ('Minh_Muas', '49974 48991 46779 46936 46491 46840 35165 44023 7038 44196 ');
INSERT INTO "user" ("name", "playlist") VALUES ('gigphuu', '40582 38951 39166 39335 39336 ');
INSERT INTO "user" ("name", "playlist") VALUES ('Leemusic139', '39357 ');
INSERT INTO "user" ("name", "playlist") VALUES ('tseem_thoj1234', '25751 35165 37144 39436 39513 39504 ');
INSERT INTO "user" ("name", "playlist") VALUES ('Hmoob_Chord', '50303 50224 49264 49265 49282 49590 49592 48540 48593 41591 ');
INSERT INTO "user" ("name", "playlist") VALUES ('Keith_YMVN', '');
INSERT INTO "user" ("name", "playlist") VALUES ('tofm2709', '40360 41692 40778 39879 28924 25273 25942 24922 28339 26221 ');
INSERT INTO "user" ("name", "playlist") VALUES ('kurotothegod', '224 30537 ');
INSERT INTO "user" ("name", "playlist") VALUES ('F7sus4', '44473 45263 41108 ');
INSERT INTO "user" ("name", "playlist") VALUES ('crush_8282', '7340 ');
INSERT INTO "user" ("name", "playlist") VALUES ('captainzozo', '27 9858 5605 15388 618 5745 249 7458 11490 11844 ');
INSERT INTO "user" ("name", "playlist") VALUES ('lethanhdat762003', '');
INSERT INTO "user" ("name", "playlist") VALUES ('phucgilm2849', '28748 26643 ');
INSERT INTO "user" ("name", "playlist") VALUES ('thinhproducer', '10715 9595 33092 27435 26194 49061 44472 47193 9616 303 ');
INSERT INTO "user" ("name", "playlist") VALUES ('nguyenhiendien111', '');
INSERT INTO "user" ("name", "playlist") VALUES ('rednguyen', '45207 10725 8626 7227 43299 43303 43300 43302 43304 43174 ');
INSERT INTO "user" ("name", "playlist") VALUES ('hoangducsmagic', '25 7178 8451 8644 17149 24967 ');
INSERT INTO "user" ("name", "playlist") VALUES ('sieubanphao', '22794 17639 6972 7206 12118 19855 19716 19263 8980 5777 ');
INSERT INTO "user" ("name", "playlist") VALUES ('hoanglespaul', '37396 31859 24721 25 35165 23907 22745 7295 5600 9808 ');
INSERT INTO "user" ("name", "playlist") VALUES ('mirotarobo10', '');
INSERT INTO "user" ("name", "playlist") VALUES ('quochuong2006', '8503 44731 44934 44730 44409 ');
INSERT INTO "user" ("name", "playlist") VALUES ('menpro58', '8512 28969 4349 45037 35359 26221 1038 41166 43276 38507 ');
INSERT INTO "user" ("name", "playlist") VALUES ('viethungnguyen002', '');
INSERT INTO "user" ("name", "playlist") VALUES ('mq149', '');
INSERT INTO "user" ("name", "playlist") VALUES ('loc01688512215', '21752 44838 3462 7974 23077 ');
INSERT INTO "user" ("name", "playlist") VALUES ('bbthaison', '49401 49399 49400 38933 39351 46096 45438 35251 45145 44023 ');
INSERT INTO "user" ("name", "playlist") VALUES ('nasa_cqt_ak11', '45179 702 43734 37665 42183 5876 43 2885 567 2620 ');
INSERT INTO "user" ("name", "playlist") VALUES ('hannie0910', '45258 5321 13881 34870 24714 14812 13116 48320 1002 47207 ');
INSERT INTO "user" ("name", "playlist") VALUES ('thangdepay', '');
INSERT INTO "user" ("name", "playlist") VALUES ('josducan216', '3929 1481 755 48295 4823 143 48011 47767 10642 2036 ');
INSERT INTO "user" ("name", "playlist") VALUES ('minhnguyet08092000', '2708 6038 32858 4010 5681 5770 2861 8839 13685 29530 ');
INSERT INTO "user" ("name", "playlist") VALUES ('nguyenthanhluan2408', '16018 ');
INSERT INTO "user" ("name", "playlist") VALUES ('DoctThien2798', '');
INSERT INTO "user" ("name", "playlist") VALUES ('nonisnicholas', '');
INSERT INTO "user" ("name", "playlist") VALUES ('huuthuc32', '17090 1842 ');
INSERT INTO "user" ("name", "playlist") VALUES ('trieuquangminh29', '9513 21940 5600 40968 22745 1920 8349 41279 35165 41085 ');
INSERT INTO "user" ("name", "playlist") VALUES ('ichigoyumi', '48827 2375 903 48301 16822 38832 45601 16253 26744 20204 ');
INSERT INTO "user" ("name", "playlist") VALUES ('grisetroseciel', '39654 439 1197 4272 1243 7637 917 29363 50173 955 ');

'''

INSERT_USER = '''INSERT INTO "user" ("name","playlist") VALUES (?,?);'''

INSERT_AUTHOR = '''INSERT INTO "singer" ("id","name") VALUES (?,?);'''

INSERT_SONG = '''INSERT INTO "song"
("id", "name", "singer_id", "rythm")
VALUES (?, ?, ?, ?);'''

class DB:

    def __init__(self,filename):
        from sqlite3 import Connection
        self.conn = Connection(filename)
        self.cur = self.conn.cursor()
        
    def init_database(self):
        self.cur.executescript(INIT_DBMS)
        self.conn.commit()
    
    def insert_song(self,record):
        self.cur.execute(INSERT_SONG,record)
        
    def insert_singer(self,record):
        self.cur.execute(INSERT_AUTHOR,record)
    
    def insert_songs(self,records):
        for record in records:
            self.insert_singer(record[1])
            self.insert_song(record[0])
        self.conn.commit()

    def insert_user(self,record):
        self.cur.execute(INSERT_USER,record)
        
    def insert_users(self,records):
        for record in records:
            self.insert_user(record)
        self.conn.commit()

    def get_users(self):
        self.cur.execute('SELECT name FROM user ;')
        records = self.cur.fetchall()
        return records
    
    def get_songs(self):
        self.cur.execute('SELECT id FROM song ;')
        records = self.cur.fetchall()
        return records

    def get_singers(self):
        self.cur.execute('SELECT id FROM singer ;')
        records = self.cur.fetchall()
        return records

    def commit(self):
        self.conn.commit()
    
    def close(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()