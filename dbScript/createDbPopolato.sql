-- --------------------------------------------------------
-- Host:                         C:\Users\marco\Desktop\Workspace\biblioteca\chinooki.sqlite
-- Versione server:              3.34.0
-- S.O. server:                  
-- HeidiSQL Versione:            11.2.0.6213
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES  */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- USE "chinooki" neither supported nor required;

-- Dump della struttura di tabella chinooki.Autore
CREATE TABLE IF NOT EXISTS "Autore" (
	"id" VARCHAR(50) NOT NULL,
	"nome" VARCHAR(50) NOT NULL,
	"cognome" VARCHAR(50) NOT NULL,
	"ddn" DATE NULL,
	"ldn" VARCHAR(50) NULL,
	"note" VARCHAR(200) NULL,
	PRIMARY KEY ("id")
);

-- Dump dei dati della tabella chinooki.Autore: -1 rows
/*!40000 ALTER TABLE "Autore" DISABLE KEYS */;
INSERT INTO "Autore" ("id", "nome", "cognome", "ddn", "ldn", "note") VALUES
	('DeGo-Ave-rda', 'Debora', 'Gornati', '1953-8-24', 'Avellino', ' AUTORE PREGENERATO - NO DESC'),
	('GiCo-Pav-pvg', 'Giada', 'Coppola', '1952-12-22', 'Pavia', ' AUTORE PREGENERATO - NO DESC'),
	('GiMa-Mon-ekw', 'Giulio', 'Marchetti', '1973-2-2', 'Montesilvano', ' AUTORE PREGENERATO - NO DESC'),
	('GiBi-Pis-dft', 'Giacomo', 'Bianchi', '1971-2-8', 'Pistoia', ' AUTORE PREGENERATO - NO DESC'),
	('ErOl-Cas-crm', 'Erika', 'Olmo', '1957-5-12', 'Caserta', ' AUTORE PREGENERATO - NO DESC'),
	('LaMa-Mod-uiq', 'Laura', 'Martino', '2005-11-25', 'Modena', ' AUTORE PREGENERATO - NO DESC'),
	('ErGi-Man-ape', 'Erica', 'Giuliani', '1985-4-26', 'Manfredonia', ' AUTORE PREGENERATO - NO DESC'),
	('JaGi-Sie-zhs', 'Jacopo', 'Giuliani', '1968-2-17', 'Siena', ' AUTORE PREGENERATO - NO DESC'),
	('GiTo-Pes-mmn', 'Giada', 'Toninelli', '1972-10-12', 'Pesaro', ' AUTORE PREGENERATO - NO DESC'),
	('PaGi-Bit-bhm', 'Paola', 'Giorgi', '2013-9-1', 'Bitonto', ' AUTORE PREGENERATO - NO DESC'),
	('AnGr-Bri-szk', 'Anna', 'Grasso', '1976-2-28', 'Brindisi', ' AUTORE PREGENERATO - NO DESC'),
	('MaMo-Bar-neq', 'Marco', 'Montanari', '1985-2-20', 'Barletta', ' AUTORE PREGENERATO - NO DESC'),
	('GaFe-Ast-hoe', 'Gabriele', 'Ferrara', '1951-12-28', 'Asti', ' AUTORE PREGENERATO - NO DESC'),
	('CaRo-Fiu-gje', 'Caterina', 'Rosso', '1953-1-19', 'Fiumicino', ' AUTORE PREGENERATO - NO DESC'),
	('AnFe-Alt-ajs', 'Antonio', 'Ferro', '1939-11-23', 'Altamura', ' AUTORE PREGENERATO - NO DESC');
/*!40000 ALTER TABLE "Autore" ENABLE KEYS */;

-- Dump della struttura di tabella chinooki.Categoria
CREATE TABLE IF NOT EXISTS "Categoria" (
	"nome" VARCHAR(50) NOT NULL UNIQUE
);

-- Dump dei dati della tabella chinooki.Categoria: -1 rows
/*!40000 ALTER TABLE "Categoria" DISABLE KEYS */;
INSERT INTO "Categoria" ("nome") VALUES
	('informatica'),
	('giallo'),
	('thriller'),
	('fantasy'),
	('fantascienza'),
	('romanzo'),
	('storia'),
	('biografia'),
	('diritto'),
	('horror');
/*!40000 ALTER TABLE "Categoria" ENABLE KEYS */;

-- Dump della struttura di tabella chinooki.categoria_restore
CREATE TABLE IF NOT EXISTS "categoria_restore" (
	"nome" VARCHAR(50) NOT NULL
);

-- Dump dei dati della tabella chinooki.categoria_restore: -1 rows
/*!40000 ALTER TABLE "categoria_restore" DISABLE KEYS */;
INSERT INTO "categoria_restore" ("nome") VALUES
	('diritto'),
	('informatica'),
	('giallo'),
	('thriller'),
	('horror'),
	('fantasy'),
	('fantascienza'),
	('romanzo'),
	('storia'),
	('biografia');
/*!40000 ALTER TABLE "categoria_restore" ENABLE KEYS */;

-- Dump della struttura di tabella chinooki.Libro
CREATE TABLE IF NOT EXISTS "Libro" (
	"isbn" VARCHAR(18) NOT NULL,
	"titolo" VARCHAR(50) NOT NULL,
	"lingua" VARCHAR(50) NULL,
	"editore" VARCHAR(50) NOT NULL,
	"annoPublicazione" DATE NOT NULL,
	"categoria" VARCHAR(50) NOT NULL,
	"copieDisponibili" INTEGER NOT NULL,
	PRIMARY KEY ("isbn"),
	CONSTRAINT "0" FOREIGN KEY ("categoria") REFERENCES "Categoria" ("nome") ON UPDATE NO ACTION ON DELETE NO ACTION
);

-- Dump dei dati della tabella chinooki.Libro: -1 rows
/*!40000 ALTER TABLE "Libro" DISABLE KEYS */;
INSERT INTO "Libro" ("isbn", "titolo", "lingua", "editore", "annoPublicazione", "categoria", "copieDisponibili") VALUES
	('080-3-2828-3617-0', 'Fardelli italiani', 'Tedesco', 'Teka Edizioni', '1995', 'Horror', 49),
	('387-1-8581-4423-5', 'RhythmJenny', 'Tedesco', 'Gambero Rosso', '1869', 'Giallo', 2),
	('034-3-6710-5013-0', 'HeartbreakandDesire', 'Italiano', 'Sanna', '1886', 'Diritto', 33),
	('914-9-4351-7920-8', 'Restoration and Sword', 'Spagnolo', 'Apice Libri', '1857', 'Informatica', 50),
	('820-6-6691-5398-5', 'GunsmokeandConsent', 'Spagnolo', 'Maschietto Editore', '1840', 'Biografia', 23),
	('423-1-3874-5921-8', 'Housekeeper''sBrand', 'Inglese', 'Kora', '1875', 'Biografia', 11),
	('350-7-4400-1601-0', 'The Facts of Blood', 'Austriaco', 'Un mondo a parte', '1940', 'Thriller', 29),
	('820-9-8075-7867-5', 'Il ladro e il duca', 'Latino', 'Pendragon', '2010', 'Informatica', 47),
	('134-7-4119-0920-2', 'TheRat''sMistress', 'Inglese', 'MathforLife', '1836', 'Giallo', 29),
	('529-7-2601-7518-8', 'Parchment and Fang', 'Tedesco', 'Orthotes', '1963', 'Thriller', 34),
	('844-3-5326-2226-1', 'RoaringPaths', 'Tedesco', 'McGraw-Hill', '1817', 'Informatica', 16),
	('900-8-3444-8539-0', 'Tiger''s Hour', 'Tedesco', 'Laboratorio Ebook Edizioni', '1966', 'Fantascienza', 29),
	('751-1-3709-5749-5', 'Assassin Prom', 'Italiano', 'Chiado Books', '1862', 'Fantascienza', 9),
	('871-8-4315-7514-8', 'Fruit for Revenge', 'Latino', 'Gangemi Editore', '1914', 'Storia', 21),
	('129-2-5822-7856-3', 'TheSignoftheCrowd', 'Spagnolo', 'Biblioteca Francescana', '1907', 'Biografia', 27),
	('929-8-2973-5576-4', 'A Poet''s Victory', 'Inglese', 'Anfora Edizioni', '2010', 'Biografia', 27),
	('925-4-8256-0360-5', 'Visconte incinta', 'Latino', 'Giuffrè', '1888', 'Romanzo', 24),
	('566-1-3739-8995-5', 'Victory''sLust', 'Tedesco', 'Blu Edizioni', '1995', 'Horror', 5),
	('962-0-8253-5516-4', 'HeartbreakandDesire', 'Tedesco', 'BeMore Edizioni', '1897', 'Biografia', 41),
	('206-8-5122-0465-8', 'Blood and Fire', 'Austriaco', 'Sandro Teti Editore', '1971', 'Diritto', 43),
	('666-2-1924-5267-1', 'Nuvole d''argento', 'Austriaco', 'Robin Edizioni', '1883', 'Romanzo', 7),
	('713-2-8777-9864-6', 'Il corso del valore', 'Austriaco', 'Stamperia Stampe Antiche', '1908', 'Storia', 27),
	('082-1-4659-7985-2', 'Housekeeper''sBrand', 'Austriaco', 'Lipa', '1927', 'Diritto', 13),
	('409-1-9091-9807-2', 'Sensual Blaze', 'Austriaco', 'Xenia', '1911', 'Fantascienza', 1),
	('649-4-4204-1722-9', 'Il mondo del sospetto', 'Spagnolo', 'Larus, Edizioni', '2011', 'Informatica', 39),
	('056-6-9857-3758-6', 'LettersofEarth', 'Italiano', 'Furetto Edizioni', '1847', 'Romanzo', 43),
	('190-6-2146-4263-4', 'L''Assassino Piumato', 'Spagnolo', 'Cliquot', '1986', 'Romanzo', 20),
	('984-8-1583-9338-9', 'Inca America', 'Tedesco', 'Nuova Italia', '1867', 'Fantasy', 43),
	('008-1-1246-7720-7', 'Un tocco di mezza estate', 'Latino', 'Bonechi', '1911', 'Diritto', 4),
	('517-8-0890-9093-0', 'BodiesofPassion', 'Latino', 'Lavieri editore', '1861', 'Horror', 7),
	('974-3-0736-0238-8', 'OtherSky', 'Inglese', 'ScantaBauchi Edizioni', '1970', 'Giallo', 23),
	('795-7-7714-5305-3', 'The Cosmic Male', 'Tedesco', 'RPlibri', '1814', 'Fantasy', 10),
	('332-6-3898-3930-4', 'Flights of Magic', 'Spagnolo', 'Tecniche Nuove', '1898', 'Informatica', 1),
	('513-9-4035-4221-0', 'The Widow of Cain', 'Latino', 'Stampalibri', '2016', 'Fantasy', 12),
	('215-2-5396-9488-3', 'OtherSky', 'Latino', 'Faust Edizioni', '1899', 'Biografia', 46),
	('262-7-8586-9318-6', 'The Homecoming Pirate', 'Italiano', 'Marotta e Cafiero Editori', '1936', 'Horror', 22),
	('518-4-4140-0289-6', 'TheWeightofDesire', 'Italiano', 'aAccademia', '1910', 'Fantascienza', 31),
	('048-8-0101-1858-6', 'Changer of Birds', 'Inglese', 'Archivi del ‘900', '1820', 'Horror', 37),
	('397-9-4355-4635-5', 'TheScepter''sCorpse', 'Tedesco', 'Furetto Edizioni', '1899', 'Romanzo', 42),
	('053-1-6396-9000-9', 'A Mother''s Duty', 'Italiano', 'Kaplan Edizioni', '1800', 'Biografia', 16),
	('331-2-0553-8600-5', 'HeartbreakandDesire', 'Spagnolo', 'Lavieri editore', '1984', 'Horror', 11),
	('454-3-0083-0924-3', 'The Widow of Cain', 'Inglese', 'Finestra, Editrice', '1959', 'Fantascienza', 3);
/*!40000 ALTER TABLE "Libro" ENABLE KEYS */;

-- Dump della struttura di tabella chinooki.LibroAutore
CREATE TABLE IF NOT EXISTS "LibroAutore" (
	"isbn" VARCHAR(50) NOT NULL,
	"id" VARCHAR(50) NOT NULL,
	CONSTRAINT "0" FOREIGN KEY ("id") REFERENCES "Autore" ("id") ON UPDATE NO ACTION ON DELETE NO ACTION,
	CONSTRAINT "1" FOREIGN KEY ("isbn") REFERENCES "Libro" ("isbn") ON UPDATE NO ACTION ON DELETE NO ACTION
);

-- Dump dei dati della tabella chinooki.LibroAutore: -1 rows
/*!40000 ALTER TABLE "LibroAutore" DISABLE KEYS */;
INSERT INTO "LibroAutore" ("isbn", "id") VALUES
	('080-3-2828-3617-0', 'PaGi-Bit-bhm'),
	('387-1-8581-4423-5', 'GiCo-Pav-pvg'),
	('034-3-6710-5013-0', 'PaGi-Bit-bhm'),
	('914-9-4351-7920-8', 'DeGo-Ave-rda'),
	('820-6-6691-5398-5', 'GiMa-Mon-ekw'),
	('423-1-3874-5921-8', 'GiCo-Pav-pvg'),
	('350-7-4400-1601-0', 'DeGo-Ave-rda'),
	('820-9-8075-7867-5', 'GiMa-Mon-ekw'),
	('134-7-4119-0920-2', 'LaMa-Mod-uiq'),
	('529-7-2601-7518-8', 'GiMa-Mon-ekw'),
	('844-3-5326-2226-1', 'CaRo-Fiu-gje'),
	('900-8-3444-8539-0', 'CaRo-Fiu-gje'),
	('751-1-3709-5749-5', 'LaMa-Mod-uiq'),
	('871-8-4315-7514-8', 'ErOl-Cas-crm'),
	('129-2-5822-7856-3', 'JaGi-Sie-zhs'),
	('929-8-2973-5576-4', 'JaGi-Sie-zhs'),
	('925-4-8256-0360-5', 'PaGi-Bit-bhm'),
	('566-1-3739-8995-5', 'ErOl-Cas-crm'),
	('962-0-8253-5516-4', 'JaGi-Sie-zhs'),
	('206-8-5122-0465-8', 'AnFe-Alt-ajs'),
	('666-2-1924-5267-1', 'LaMa-Mod-uiq'),
	('713-2-8777-9864-6', 'AnGr-Bri-szk'),
	('082-1-4659-7985-2', 'ErGi-Man-ape'),
	('409-1-9091-9807-2', 'AnGr-Bri-szk'),
	('649-4-4204-1722-9', 'GiBi-Pis-dft'),
	('056-6-9857-3758-6', 'CaRo-Fiu-gje'),
	('190-6-2146-4263-4', 'GaFe-Ast-hoe'),
	('984-8-1583-9338-9', 'JaGi-Sie-zhs'),
	('008-1-1246-7720-7', 'GaFe-Ast-hoe'),
	('517-8-0890-9093-0', 'MaMo-Bar-neq'),
	('974-3-0736-0238-8', 'GiCo-Pav-pvg'),
	('795-7-7714-5305-3', 'CaRo-Fiu-gje'),
	('332-6-3898-3930-4', 'AnFe-Alt-ajs'),
	('513-9-4035-4221-0', 'AnFe-Alt-ajs'),
	('215-2-5396-9488-3', 'CaRo-Fiu-gje'),
	('262-7-8586-9318-6', 'ErGi-Man-ape'),
	('518-4-4140-0289-6', 'GiCo-Pav-pvg'),
	('048-8-0101-1858-6', 'AnFe-Alt-ajs'),
	('397-9-4355-4635-5', 'JaGi-Sie-zhs'),
	('053-1-6396-9000-9', 'AnFe-Alt-ajs'),
	('331-2-0553-8600-5', 'ErGi-Man-ape'),
	('454-3-0083-0924-3', 'GiCo-Pav-pvg');
/*!40000 ALTER TABLE "LibroAutore" ENABLE KEYS */;

-- Dump della struttura di tabella chinooki.LibroCategoria
CREATE TABLE IF NOT EXISTS "LibroCategoria" (
	"isbn" VARCHAR(50) NOT NULL,
	"categoria" VARCHAR(50) NOT NULL,
	CONSTRAINT "FK__Libro" FOREIGN KEY ("isbn") REFERENCES "Libro" ("isbn"),
	CONSTRAINT "FK__Categoria" FOREIGN KEY ("categoria") REFERENCES "Categoria" ("nome")
);

-- Dump dei dati della tabella chinooki.LibroCategoria: -1 rows
/*!40000 ALTER TABLE "LibroCategoria" DISABLE KEYS */;
INSERT INTO "LibroCategoria" ("isbn", "categoria") VALUES
	('080-3-2828-3617-0', 'Horror'),
	('387-1-8581-4423-5', 'Giallo'),
	('034-3-6710-5013-0', 'Diritto'),
	('914-9-4351-7920-8', 'Informatica'),
	('820-6-6691-5398-5', 'Biografia'),
	('423-1-3874-5921-8', 'Biografia'),
	('350-7-4400-1601-0', 'Thriller'),
	('820-9-8075-7867-5', 'Informatica'),
	('134-7-4119-0920-2', 'Giallo'),
	('529-7-2601-7518-8', 'Thriller'),
	('844-3-5326-2226-1', 'Informatica'),
	('900-8-3444-8539-0', 'Fantascienza'),
	('751-1-3709-5749-5', 'Fantascienza'),
	('871-8-4315-7514-8', 'Storia'),
	('129-2-5822-7856-3', 'Biografia'),
	('929-8-2973-5576-4', 'Biografia'),
	('925-4-8256-0360-5', 'Romanzo'),
	('566-1-3739-8995-5', 'Horror'),
	('962-0-8253-5516-4', 'Biografia'),
	('206-8-5122-0465-8', 'Diritto'),
	('666-2-1924-5267-1', 'Romanzo'),
	('713-2-8777-9864-6', 'Storia'),
	('082-1-4659-7985-2', 'Diritto'),
	('409-1-9091-9807-2', 'Fantascienza'),
	('649-4-4204-1722-9', 'Informatica'),
	('056-6-9857-3758-6', 'Romanzo'),
	('190-6-2146-4263-4', 'Romanzo'),
	('984-8-1583-9338-9', 'Fantasy'),
	('008-1-1246-7720-7', 'Diritto'),
	('517-8-0890-9093-0', 'Horror'),
	('974-3-0736-0238-8', 'Giallo'),
	('795-7-7714-5305-3', 'Fantasy'),
	('332-6-3898-3930-4', 'Informatica'),
	('513-9-4035-4221-0', 'Fantasy'),
	('215-2-5396-9488-3', 'Biografia'),
	('262-7-8586-9318-6', 'Horror'),
	('518-4-4140-0289-6', 'Fantascienza'),
	('048-8-0101-1858-6', 'Horror'),
	('397-9-4355-4635-5', 'Romanzo'),
	('053-1-6396-9000-9', 'Biografia'),
	('331-2-0553-8600-5', 'Horror'),
	('454-3-0083-0924-3', 'Fantascienza');
/*!40000 ALTER TABLE "LibroCategoria" ENABLE KEYS */;

-- Dump della struttura di tabella chinooki.PrestitiAttivi
CREATE TABLE IF NOT EXISTS "PrestitiAttivi" (
	"tessera" VARCHAR(50) NOT NULL UNIQUE,
	"num" INTEGER NOT NULL,
	CONSTRAINT "0" FOREIGN KEY ("tessera") REFERENCES "Utenti" ("tessera") ON UPDATE NO ACTION ON DELETE NO ACTION
);

-- Dump dei dati della tabella chinooki.PrestitiAttivi: -1 rows
/*!40000 ALTER TABLE "PrestitiAttivi" DISABLE KEYS */;
INSERT INTO "PrestitiAttivi" ("tessera", "num") VALUES
	('56055-vug', 0),
	('96049-pwt', 0),
	('70969-bgg', 0),
	('35731-rpi', 0),
	('87845-txe', 0),
	('13286-vfa', 0),
	('09092-jpn', 0),
	('88217-dcm', 0),
	('37560-qhq', 0),
	('03487-sgp', 0),
	('41813-gul', 0),
	('02869-nex', 0),
	('48776-uvu', 0),
	('45388-saw', 0);
/*!40000 ALTER TABLE "PrestitiAttivi" ENABLE KEYS */;

-- Dump della struttura di tabella chinooki.Prestito
CREATE TABLE IF NOT EXISTS "Prestito" (
	"tesseraUtente" VARCHAR(50) NOT NULL,
	"dataInizio" DATE NOT NULL,
	"dataConsegna" DATE NULL,
	"isbn" VARCHAR(50) NOT NULL,
	"quantita" INTEGER NOT NULL,
	"id" INTEGER NOT NULL,
	"ritardo" INTEGER NULL,
	PRIMARY KEY ("id"),
	CONSTRAINT "0" FOREIGN KEY ("isbn") REFERENCES "Libro" ("isbn") ON UPDATE NO ACTION ON DELETE NO ACTION,
	CONSTRAINT "1" FOREIGN KEY ("tesseraUtente") REFERENCES "Utenti" ("tessera") ON UPDATE NO ACTION ON DELETE NO ACTION
);

-- Dump dei dati della tabella chinooki.Prestito: -1 rows
/*!40000 ALTER TABLE "Prestito" DISABLE KEYS */;
/*!40000 ALTER TABLE "Prestito" ENABLE KEYS */;

-- Dump della struttura di tabella chinooki.titoli_template
CREATE TABLE IF NOT EXISTS "titoli_template" (
	"Titolo" VARCHAR(150) NULL
);

-- Dump dei dati della tabella chinooki.titoli_template: -1 rows
/*!40000 ALTER TABLE "titoli_template" DISABLE KEYS */;
INSERT INTO "titoli_template" ("Titolo") VALUES
	('TheRevengeofTragedy'),
	('TheChild''sCorps'),
	('ThePuzzleinthePond'),
	('EnchantingRivers'),
	('AWebofBelief'),
	('BodiesofPassion'),
	('GunsmokeandConsent'),
	('ThePromiseofDetroit'),
	('RoaringPaths'),
	('HeartbreakandDesire'),
	('CharlieandtheCompass'),
	('AccusedbyError'),
	('TheRat''sMistress'),
	('HolyColors'),
	('WarmCommand'),
	('Victory''sLust'),
	('SeasideOrphans'),
	('AFreshPath'),
	('SunriseofYesterday'),
	('TheGiant''sClub'),
	('FoolishMasks'),
	('LettersofEarth'),
	('TheLegacyoftheApprentice'),
	('TheKingmaker''sNose'),
	('Sleeper''sCommand'),
	('AHauntedFlesh'),
	('TheSleuthoftheHive'),
	('DadontheWall'),
	('AFeastofExile'),
	('RhythmJenny'),
	('TheRoarofthePearl'),
	('KnifeTight'),
	('MercuryHidden'),
	('TheScepter''sCorpse'),
	('AWaywardThunder'),
	('TheWeightofDesire'),
	('HavenoftheHall'),
	('Housekeeper''sBrand'),
	('BlackshirttheMouse'),
	('TheSunatEvening'),
	('Patriot''sWedge'),
	('EyesoftheMesa'),
	('OtherSky'),
	('TheSignoftheCrowd'),
	('TheShatteredProphecy'),
	('TheFellowshipoftheMoment'),
	('AnInescapableDeception'),
	('HiddenSwitch'),
	('TheRevengeofTragedy'),
	('TheChild''sCorps'),
	('ThePuzzleinthePond'),
	('EnchantingRivers'),
	('AWebofBelief'),
	('BodiesofPassion'),
	('GunsmokeandConsent'),
	('ThePromiseofDetroit'),
	('RoaringPaths'),
	('HeartbreakandDesire'),
	('CharlieandtheCompass'),
	('AccusedbyError'),
	('TheRat''sMistress'),
	('HolyColors'),
	('WarmCommand'),
	('Victory''sLust'),
	('SeasideOrphans'),
	('AFreshPath'),
	('SunriseofYesterday'),
	('TheGiant''sClub'),
	('FoolishMasks'),
	('LettersofEarth'),
	('TheLegacyoftheApprentice'),
	('TheKingmaker''sNose'),
	('Sleeper''sCommand'),
	('AHauntedFlesh'),
	('TheSleuthoftheHive'),
	('DadontheWall'),
	('AFeastofExile'),
	('RhythmJenny'),
	('TheRoarofthePearl'),
	('KnifeTight'),
	('MercuryHidden'),
	('TheScepter''sCorpse'),
	('AWaywardThunder'),
	('TheWeightofDesire'),
	('HavenoftheHall'),
	('Housekeeper''sBrand'),
	('BlackshirttheMouse'),
	('TheSunatEvening'),
	('Patriot''sWedge'),
	('EyesoftheMesa'),
	('OtherSky'),
	('TheSignoftheCrowd'),
	('TheShatteredProphecy'),
	('TheFellowshipoftheMoment'),
	('AnInescapableDeception'),
	('HiddenSwitch'),
	('An Improper Day'),
	('The Schemes of Idleness'),
	('Sister for Panic'),
	('Simple Relics'),
	('The Senator''s Test'),
	('Tunnel of Pearls'),
	('The Cosmic Male'),
	('A Night of Rage'),
	('Stormy Stone'),
	('Necessary Brand'),
	('Fruit for Revenge'),
	('Crack Lightning'),
	('A Sunset Dose'),
	('American Missing'),
	('Robot''s Planet'),
	('The Force of Glamour'),
	('Wild and Jake'),
	('Prairie Husbands'),
	('Time and Burning'),
	('Regency Tight'),
	('Pig Indulgence'),
	('Fall of the Faith'),
	('Brand of the River'),
	('Wicked Sarah'),
	('Danger Sinner'),
	('Goliath and the Earl'),
	('Counter Bliss'),
	('Changer of Birds'),
	('The Mystery of the World'),
	('Team Dune'),
	('A Disappearance in Spain'),
	('The Course of the House'),
	('Butterflies in the Moonlight'),
	('Accused by Proxy'),
	('Invincible Road'),
	('Jonathan and Shadow'),
	('Jason''s Dilemma'),
	('An Accidental Bouquet'),
	('Maid of Promise'),
	('Evidence of Delight'),
	('Sworn Bargains'),
	('Tennessee Goodbye'),
	('Flying Sisters'),
	('Satin Ships'),
	('Rogues in the Afterglow'),
	('Restoration and Sword'),
	('An Ancient Hero'),
	('The Shamrock Cake'),
	('Newport Virgins'),
	('Warm Schemes'),
	('Washington Reluctant'),
	('Simon the Apple'),
	('Hidden Bonds'),
	('The Widow of Cain'),
	('The Storms of Sleep'),
	('The Dead of Peace'),
	('The Martian Lake'),
	('Tiger''s Hour'),
	('Nanny and the Bandit'),
	('Vampire Rebellion'),
	('Inhuman Armies'),
	('Doctors in Logic'),
	('A Rake for Deliverance'),
	('A Hometown Deceiver'),
	('The Machine''s Visitor'),
	('Goliath and the Earl'),
	('Magician''s Palace'),
	('The Telltale Key'),
	('The Rings of Time'),
	('Assassin Prom'),
	('Sensual Blaze'),
	('Soldier''s Mistral'),
	('The Neon Prize'),
	('Tony''s Wyoming'),
	('Portrait in Berlin'),
	('Unknown Adventures'),
	('Addie and the Jubilee'),
	('Visible Harbour'),
	('Parchment and Fang'),
	('Inca America'),
	('Bodies of Amber'),
	('Taste of a Scandal'),
	('The Captive''s Passion'),
	('The Heart''s Nest'),
	('Blood and Fire'),
	('Beckoning Engines'),
	('Defender of the Deceiver'),
	('Baby on the Town'),
	('The Mermaid''s Pact'),
	('Ivory Jump'),
	('Flights of Magic'),
	('The Heir of the Pearl'),
	('Brief Whale'),
	('A Regency Moment'),
	('Set in Bed'),
	('Circumstantial David'),
	('Brain Sins'),
	('The Listening Bomb'),
	('River of Echoes'),
	('The Monk''s Club'),
	('The Falcon''s Intrigue'),
	('Thief''s Kin'),
	('Venom''s Bounty'),
	('Incident on Show'),
	('A Poet''s Victory'),
	('The Summer''s Demand'),
	('A Knight''s Persuasion'),
	('Misfortune March'),
	('The Power Dreams'),
	('A Reckless Feast'),
	('The Heart''s Nest'),
	('Wedding Substitute'),
	('A Lord for Justice'),
	('Saturday''s Ship'),
	('Acts of Possession'),
	('The Traveller in Faerie'),
	('The Tudor Hunter'),
	('The Horse''s Nanny'),
	('Dreaming in Danger'),
	('Sunset and the Spinster'),
	('A Streak of Mary'),
	('K and Child'),
	('A Harvest of Honour'),
	('The Honest Afternoon'),
	('Masks of the Mist'),
	('A Mother''s Duty'),
	('Teller of Friends'),
	('The Princess and the Prince'),
	('Stranger''s Harvest'),
	('Phantom Outsider'),
	('Cavanaugh Crushed'),
	('Empty Devil'),
	('Dragon Houses'),
	('Healer''s Bounty'),
	('A Madcap Question'),
	('Lady Shuffle'),
	('The Facts of Blood'),
	('Emily and the Tenderfoot'),
	('Casey''s Errand'),
	('Hermit on Sunday'),
	('Carnage of the Moment'),
	('The Homecoming Pirate'),
	('A Relative Infatuation'),
	('Bodyguard of Stairs'),
	('L''Oracolo dei Denti'),
	('Spettro della profezia'),
	('Trovato Whale'),
	('Risoluzione Iv'),
	('Canaglia per Nessuno'),
	('Papà in laurea'),
	('Il Briar e il George'),
	('La volontà e il guerriero'),
	('Nice Knight'),
	('Ferite di settembre'),
	('Uomo inattivo'),
	('Cava rigida'),
	('Il regno della vendetta'),
	('L''ostaggio della fanciulla'),
	('Dolci aspettative'),
	('L''Assassino Piumato'),
	('Earth Gallant'),
	('Il colore dell''anima'),
	('La portata di un patriota'),
	('Un papà per Caruso'),
	('Il nodo dello stallone'),
	('Mary''s Room'),
	('Il viale del lupo'),
	('Blackbird Cove'),
	('Sorella dell''Eclissi'),
	('Una persona di perfezione'),
	('Il bisturi dell''umanità'),
	('Halcyon Enterprise'),
	('Segni di pioggia'),
	('Il Maverick Shock'),
	('The Rabbit Trust'),
	('Heroes of Blackshirt'),
	('Qualcosa di colore'),
	('Gli dei della libertà'),
	('Scandalo a Rust'),
	('Amato manufatto'),
	('Tempesta del Duca'),
	('Angelo di Windows'),
	('Sacerdotessa rossa'),
	('Assenza di autunno'),
	('La fuga precipitosa di Jenna'),
	('Il chiamante nel pupazzo di neve'),
	('Robot''s Planet'),
	('Frontier Dune'),
	('Il fuorilegge e la spia'),
	('Desiderio ribelle'),
	('Fiori strappati'),
	('Una sete di dinosauro '),
	('Chiama Prescelti'),
	('Il viaggio Earl'),
	('Un tocco di mezza estate'),
	('Nuvole d''argento'),
	('Tocco di rischio'),
	('Il ladro e il duca'),
	('Scene d''estate'),
	('La collana della montagna'),
	('Il mondo del sospetto'),
	('The Sweetheart Halo'),
	('Mummia di seta'),
	('The Mirror Kid'),
	('Nubi nemiche'),
	('La volpe allo specchio'),
	('Frutto appassionato'),
	('L''indiscrezione del pagano'),
	('Riti di verità'),
	('Glen politico'),
	('L''anima del parroco'),
	('Discepoli del mattino'),
	('Visconte incinta'),
	('Strade di sospetto'),
	('Una madre per Caruso'),
	('Sorelle volanti'),
	('Reso per corrispondenza'),
	('Corpus Stiff'),
	('La magia di un cugino'),
	('Una canzone per Marietta'),
	('L''aquila nella siepe'),
	('The Camelot Darkness'),
	('Il presidente prodigo'),
	('La spina e l''orso'),
	('Figlia della flotta'),
	('Sogni del lupo'),
	('Oregon Enigma'),
	('Bound Shame'),
	('Mani di casa'),
	('Un giardino nella polvere'),
	('Viola sulla soglia'),
	('Hitler Clear'),
	('La distruzione del triangolo'),
	('Essenza di una strega'),
	('Il corso del valore'),
	('L''interruttore dei problemi'),
	('Fardelli italiani'),
	('Mare di benedizioni'),
	('Negozio delle fortune'),
	('Morrigan in transito ');
/*!40000 ALTER TABLE "titoli_template" ENABLE KEYS */;

-- Dump della struttura di tabella chinooki.Utenti
CREATE TABLE IF NOT EXISTS "Utenti" (
	"tessera" VARCHAR(15) NOT NULL,
	"nome" VARCHAR(50) NOT NULL,
	"cognome" VARCHAR(50) NOT NULL,
	"data_registrazione" DATE NOT NULL,
	"telefono" VARCHAR(12) NULL UNIQUE,
	"indirizzo" VARCHAR(50) NULL,
	"email" VARCHAR(50) NULL UNIQUE,
	PRIMARY KEY ("tessera")
);

-- Dump dei dati della tabella chinooki.Utenti: -1 rows
/*!40000 ALTER TABLE "Utenti" DISABLE KEYS */;
INSERT INTO "Utenti" ("tessera", "nome", "cognome", "data_registrazione", "telefono", "indirizzo", "email") VALUES
	('56055-vug', 'Michele', 'Monti', '2007-4-23', '398421236436', 'viale Brisa 24', 'MicheMo@ms.com'),
	('96049-pwt', 'Lorenzo', 'Fiore', '2014-9-21', '393199656543', 'viale contrada degli Olocati 1', 'LoFio@protonmail.com'),
	('70969-bgg', 'Sara', 'Gornati', '2020-7-2', '394719115649', 'strada dei Piatti 31', 'SGorn@gmail.com'),
	('35731-rpi', 'Luca', 'Rossi', '1945-12-8', '394154835541', 'viale Bergamo 33', 'LRoss@protonmail.com'),
	('87845-txe', 'Jacopo', 'Gornati', '1939-9-1', '397418128600', 'via Melone 45', 'JacG@aruba.com'),
	('13286-vfa', 'Roberta', 'De Luca', '1945-10-5', '390549489269', 'via Zara 37', 'RoDe L@hostIt.com'),
	('09092-jpn', 'Stefano', 'Minardi', '2010-3-8', '390037789166', 'viale Cusani 23', 'StefaMin@airmail.com'),
	('88217-dcm', 'Elisa', 'D''angelo', '2012-6-23', '392692181235', 'strada Rasini 12', 'ElD''a@hostIt.com'),
	('37560-qhq', 'Claudio', 'Franco', '1955-10-16', '393745067410', 'piazza Medici 28', 'ClauFranc@hostIt.com'),
	('03487-sgp', 'Leonardo', 'Ferro', '1943-7-1', '397490021899', 'pz.le Della Sala 21', 'LeoFerr@airmail.com'),
	('41813-gul', 'Gaia', 'Parisi', '2020-5-19', '396987193172', 'pz.le Sauro 42', 'GP@aruba.com'),
	('02869-nex', 'Riccardo', 'De Cristofaro', '1931-4-8', '399284233117', 'via Cavenaghi 10', 'RiccarDe Cri@mymail.com'),
	('48776-uvu', 'Edoardo', 'Marchetti', '1977-10-13', '396223262626', 'pz.le Frontini 26', 'EdMarche@outlook.com'),
	('45388-saw', 'Silvia', 'Costa', '1983-6-3', '397900319946', 'viale del Leoncino 24', 'SiC@apple.com');
/*!40000 ALTER TABLE "Utenti" ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;