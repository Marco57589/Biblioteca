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
/*!40000 ALTER TABLE "LibroCategoria" ENABLE KEYS */;

-- Dump della struttura di tabella chinooki.PrestitiAttivi
CREATE TABLE IF NOT EXISTS "PrestitiAttivi" (
	"tessera" VARCHAR(50) NOT NULL UNIQUE,
	"num" INTEGER NOT NULL,
	CONSTRAINT "0" FOREIGN KEY ("tessera") REFERENCES "Utenti" ("tessera") ON UPDATE NO ACTION ON DELETE NO ACTION
);

-- Dump dei dati della tabella chinooki.PrestitiAttivi: -1 rows
/*!40000 ALTER TABLE "PrestitiAttivi" DISABLE KEYS */;
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
/*!40000 ALTER TABLE "Utenti" ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
