CREATE DATABASE  IF NOT EXISTS `imsapp` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `imsapp`;
-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: localhost    Database: imsapp
-- ------------------------------------------------------
-- Server version	5.7.22-0ubuntu0.17.10.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Temporary table structure for view `vwCompnayInfo`
--

DROP TABLE IF EXISTS `vwCompnayInfo`;
/*!50001 DROP VIEW IF EXISTS `vwCompnayInfo`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `vwCompnayInfo` AS SELECT 
 1 AS `BranchName`,
 1 AS `Address`,
 1 AS `PhoneNumber`,
 1 AS `Email`,
 1 AS `GSTNo`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `VwInvoiceDetails`
--

DROP TABLE IF EXISTS `VwInvoiceDetails`;
/*!50001 DROP VIEW IF EXISTS `VwInvoiceDetails`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `VwInvoiceDetails` AS SELECT 
 1 AS `BBranchName`,
 1 AS `BAddress`,
 1 AS `BState`,
 1 AS `BCountry`,
 1 AS `BIsMainBranch`,
 1 AS `BSalesGL`,
 1 AS `BEmail`,
 1 AS `BGSTNo`,
 1 AS `BPhoneNumber`,
 1 AS `InvoiceNumber`,
 1 AS `CustomerNumber`,
 1 AS `CustomerName`,
 1 AS `GstNumber`,
 1 AS `Address`,
 1 AS `Email`,
 1 AS `PhoneNumber`,
 1 AS `InvoiceDate`,
 1 AS `InvoiceType`,
 1 AS `PaymentDueDate`,
 1 AS `StateCode`,
 1 AS `RepName`,
 1 AS `PaymentTerms`,
 1 AS `FrieghtTerms`,
 1 AS `DeliveryTerms`,
 1 AS `Transporter`,
 1 AS `TransportMode`,
 1 AS `EsugamaNo`,
 1 AS `Destination`,
 1 AS `LRNoAndDate`,
 1 AS `ExpectedDelivery`,
 1 AS `NoOfPacks`,
 1 AS `EnteredDate`,
 1 AS `RoundOff`,
 1 AS `EnteredBy`,
 1 AS `BalanceAmount`,
 1 AS `TransactionDate`,
 1 AS `ITotalAmount`,
 1 AS `ITaxAmount`,
 1 AS `GrossWeight`,
 1 AS `ProductName`,
 1 AS `ProductCode`,
 1 AS `Description`,
 1 AS `HsnSacCode`,
 1 AS `Units`,
 1 AS `OrderQty`,
 1 AS `CGST`,
 1 AS `SGST`,
 1 AS `DiscountAmt`,
 1 AS `GrossAmount`,
 1 AS `TaxPerProductAmt`,
 1 AS `TaxPerProduct`,
 1 AS `TotalAmount`,
 1 AS `Discount`,
 1 AS `UnitPrice`,
 1 AS `Color`,
 1 AS `CrDrNote`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `vwGstSummary`
--

DROP TABLE IF EXISTS `vwGstSummary`;
/*!50001 DROP VIEW IF EXISTS `vwGstSummary`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `vwGstSummary` AS SELECT 
 1 AS `InvoiceNumber`,
 1 AS `TaxType`,
 1 AS `TaxPerProduct`,
 1 AS `TotalGST`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `VwProductStockDetails`
--

DROP TABLE IF EXISTS `VwProductStockDetails`;
/*!50001 DROP VIEW IF EXISTS `VwProductStockDetails`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `VwProductStockDetails` AS SELECT 
 1 AS `ProductCode`,
 1 AS `ProductName`,
 1 AS `ProductID`,
 1 AS `CategoryName`,
 1 AS `ProdCatDesc`,
 1 AS `AvailableQty`,
 1 AS `UnitPrice`,
 1 AS `FinalPrice`,
 1 AS `Image`,
 1 AS `ImageString`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `vwCompnayInfo`
--

/*!50001 DROP VIEW IF EXISTS `vwCompnayInfo`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vwCompnayInfo` AS select `mod_auth_branchdetails`.`BranchName` AS `BranchName`,`mod_auth_branchdetails`.`Address` AS `Address`,`mod_auth_branchdetails`.`PhoneNumber` AS `PhoneNumber`,`mod_auth_branchdetails`.`Email` AS `Email`,`mod_auth_branchdetails`.`GSTNo` AS `GSTNo` from `mod_auth_branchdetails` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `VwInvoiceDetails`
--

/*!50001 DROP VIEW IF EXISTS `VwInvoiceDetails`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `VwInvoiceDetails` AS select coalesce(`mod_auth_branchdetails`.`BranchName`,'') AS `BBranchName`,coalesce(`mod_auth_branchdetails`.`Address`,'') AS `BAddress`,coalesce(`mod_auth_branchdetails`.`State`,'') AS `BState`,coalesce(`mod_auth_branchdetails`.`Country`,'') AS `BCountry`,coalesce(`mod_auth_branchdetails`.`IsMainBranch`,'') AS `BIsMainBranch`,coalesce(`mod_auth_branchdetails`.`SalesGL`,'') AS `BSalesGL`,coalesce(`mod_auth_branchdetails`.`Email`,'') AS `BEmail`,coalesce(`mod_auth_branchdetails`.`GSTNo`,'') AS `BGSTNo`,coalesce(`mod_auth_branchdetails`.`PhoneNumber`,'') AS `BPhoneNumber`,coalesce(`billing_invoicedetails`.`InvoiceNumber`,'') AS `InvoiceNumber`,coalesce(`customer_customerdetails`.`CustomerNumber`,'') AS `CustomerNumber`,coalesce(`customer_customerdetails`.`CustomerName`,'') AS `CustomerName`,coalesce(`customer_customerdetails`.`GstNumber`,'') AS `GstNumber`,coalesce(`customer_customeraddress`.`Address`,'') AS `Address`,coalesce(`customer_customeraddress`.`Email`,'') AS `Email`,coalesce(`customer_customeraddress`.`PhoneNumber`,'') AS `PhoneNumber`,`billing_invoicedetails`.`InvoiceDate` AS `InvoiceDate`,coalesce(`billing_invoicedetails`.`InvoiceType`,'') AS `InvoiceType`,`billing_invoicedetails`.`PaymentDueDate` AS `PaymentDueDate`,coalesce(`billing_invoicedetails`.`StateCode`,'') AS `StateCode`,coalesce(`billing_invoicedetails`.`RepName`,'') AS `RepName`,coalesce(`billing_invoicedetails`.`PaymentTerms`,'') AS `PaymentTerms`,coalesce(`billing_invoicedetails`.`FrieghtTerms`,'') AS `FrieghtTerms`,coalesce(`billing_invoicedetails`.`DeliveryTerms`,'') AS `DeliveryTerms`,coalesce(`billing_invoicedetails`.`Transporter`,'') AS `Transporter`,coalesce(`billing_invoicedetails`.`TransportMode`,'') AS `TransportMode`,coalesce(`billing_invoicedetails`.`EsugamaNo`,'') AS `EsugamaNo`,coalesce(`billing_invoicedetails`.`Destination`,'') AS `Destination`,coalesce(`billing_invoicedetails`.`LRNoAndDate`,'') AS `LRNoAndDate`,`billing_invoicedetails`.`ExpectedDelivery` AS `ExpectedDelivery`,coalesce(`billing_invoicedetails`.`NoOfPacks`,'') AS `NoOfPacks`,coalesce(`billing_invoicedetails`.`EnteredDate`,'') AS `EnteredDate`,coalesce(`billing_invoicedetails`.`RoundOff`,'') AS `RoundOff`,coalesce(`billing_invoicedetails`.`EnteredBy`,'') AS `EnteredBy`,coalesce(`billing_invoicedetails`.`BalanceAmount`,'') AS `BalanceAmount`,`billing_invoicedetails`.`TransactionDate` AS `TransactionDate`,coalesce(`billing_invoicedetails`.`TotalAmount`,'') AS `ITotalAmount`,coalesce(`billing_invoicedetails`.`TaxAmount`,'') AS `ITaxAmount`,coalesce(`billing_invoicedetails`.`GrossWeight`,'') AS `GrossWeight`,coalesce(`inventory_products`.`ProductName`,'') AS `ProductName`,coalesce(`inventory_products`.`ProductCode`,'') AS `ProductCode`,coalesce(`inventory_products`.`Description`,'') AS `Description`,coalesce(`inventory_products`.`HsnSacCode`,'') AS `HsnSacCode`,coalesce(`inventory_products`.`Units`,'') AS `Units`,`ordermanagement_orderdetails`.`OrderQty` AS `OrderQty`,(`ordermanagement_orderdetails`.`TaxPerProduct` / 2) AS `CGST`,(`ordermanagement_orderdetails`.`TaxPerProduct` / 2) AS `SGST`,(((`ordermanagement_orderdetails`.`OrderQty` * `ordermanagement_orderdetails`.`UnitPrice`) * `ordermanagement_orderdetails`.`Discount`) / 100) AS `DiscountAmt`,((`ordermanagement_orderdetails`.`OrderQty` * `ordermanagement_orderdetails`.`UnitPrice`) - (((`ordermanagement_orderdetails`.`OrderQty` * `ordermanagement_orderdetails`.`UnitPrice`) * `ordermanagement_orderdetails`.`Discount`) / 100)) AS `GrossAmount`,(((((`ordermanagement_orderdetails`.`OrderQty` * `ordermanagement_orderdetails`.`UnitPrice`) - (((`ordermanagement_orderdetails`.`OrderQty` * `ordermanagement_orderdetails`.`UnitPrice`) * `ordermanagement_orderdetails`.`Discount`) / 100)) * `ordermanagement_orderdetails`.`TaxPerProduct`) / 100) / 2) AS `TaxPerProductAmt`,`ordermanagement_orderdetails`.`TaxPerProduct` AS `TaxPerProduct`,`ordermanagement_orderdetails`.`TotalAmount` AS `TotalAmount`,`ordermanagement_orderdetails`.`Discount` AS `Discount`,`ordermanagement_orderdetails`.`UnitPrice` AS `UnitPrice`,coalesce(`inventory_products`.`Color`,'') AS `Color`,coalesce(`billing_invoicedetails`.`CrDrNote`,0) AS `CrDrNote` from (((`billing_invoicedetails` join `mod_auth_branchdetails`) join (`customer_customeraddress` join `customer_customerdetails` on((`customer_customeraddress`.`CustomerID_id` = `customer_customerdetails`.`CustomerID`)))) join ((`ordermanagement_orderdetails` join `ordermanagement_manageorder` on((`ordermanagement_orderdetails`.`OrderNumber_id` = `ordermanagement_manageorder`.`OrderNumber`))) join `inventory_products` on((`ordermanagement_orderdetails`.`ProductCode_id` = `inventory_products`.`ProductID`)))) where ((`billing_invoicedetails`.`CustomerNumber` = `customer_customerdetails`.`CustomerNumber`) and (`ordermanagement_manageorder`.`GeneratedOrderNumber` = `billing_invoicedetails`.`GeneratedOrderNumber`) and (`inventory_products`.`ProductID` = `ordermanagement_orderdetails`.`ProductCode_id`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vwGstSummary`
--

/*!50001 DROP VIEW IF EXISTS `vwGstSummary`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vwGstSummary` AS select `INV`.`InvoiceNumber` AS `InvoiceNumber`,'GST' AS `TaxType`,`od`.`TaxPerProduct` AS `TaxPerProduct`,(select ((((`od1`.`UnitPrice` * `od1`.`OrderQty`) - (((`od1`.`UnitPrice` * `od1`.`OrderQty`) * `od1`.`Discount`) / 100)) * `od1`.`TaxPerProduct`) / 100) from `ordermanagement_orderdetails` `od1` where ((`od1`.`OrderNumber_id` = `od`.`OrderNumber_id`) and (`od1`.`ProductCode_id` = `od`.`ProductCode_id`))) AS `TotalGST` from ((`ordermanagement_manageorder` `mo` join `ordermanagement_orderdetails` `od` on((`mo`.`OrderNumber` = `od`.`OrderNumber_id`))) join `billing_invoicedetails` `INV` on((`INV`.`GeneratedOrderNumber` = `mo`.`GeneratedOrderNumber`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `VwProductStockDetails`
--

/*!50001 DROP VIEW IF EXISTS `VwProductStockDetails`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `VwProductStockDetails` AS select `prd`.`ProductCode` AS `ProductCode`,`prd`.`ProductName` AS `ProductName`,`prd`.`ProductID` AS `ProductID`,`pc`.`CategoryName` AS `CategoryName`,`pc`.`Description` AS `ProdCatDesc`,`stock`.`AvailableQty` AS `AvailableQty`,`prd_price`.`UnitPrice` AS `UnitPrice`,`prd_price`.`FinalPrice` AS `FinalPrice`,`prd`.`Image` AS `Image`,substr(`prd`.`Image`,24,length(`prd`.`Image`)) AS `ImageString` from (((`inventory_stockdetails` `stock` join `inventory_products` `prd` on((`stock`.`ProductID_id` = `prd`.`ProductID`))) left join `inventory_productprice` `prd_price` on((`prd_price`.`ProductID_id` = `prd`.`ProductID`))) join `inventory_productcategory` `pc` on((`pc`.`id` = `prd`.`CategoryCode_id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Dumping events for database 'imsapp'
--

--
-- Dumping routines for database 'imsapp'
--
/*!50003 DROP FUNCTION IF EXISTS `AmountToWords` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` FUNCTION `AmountToWords`(
    `nAmount` DECIMAL(11,2)) RETURNS varchar(2000) CHARSET utf8
BEGIN

DECLARE AMT_Words   VARCHAR(2000) ;
DECLARE AMT_Text1   VARCHAR(2000) ;
DECLARE AMT_Text2   VARCHAR(2000) ;
DECLARE AMT_Text3   VARCHAR(2000) ;
DECLARE Words          VARCHAR(2000) ;
DECLARE Rupee_Txt      VARCHAR(2000) ;
DECLARE RupeeTxt      VARCHAR(2000) ;
DECLARE SP_Txt1      VARCHAR(2000) ;
DECLARE SP_Txt2      VARCHAR(2000) ;
DECLARE SP_Txt3      VARCHAR(2000) ;
DECLARE Decimal_Txt VARCHAR(20)      ;

DECLARE WP              INT;
DECLARE SP              INT;
DECLARE RLEN          INT;
DECLARE PLEN        INT;
DECLARE _Rupee          INT;
DECLARE _Decimal      INT;
   
   
    SET AMT_Words   = '';
    SET AMT_Text1   = ' One ,Two ,Three ,Four ,Five ,Six ,Seven ,Eight ,Nine ,Ten ';
    SET AMT_Text1   = CONCAT(AMT_Text1,',Eleven ,Twelve ,Thirteen ,Forteen ,Fifteen ,Sixteen ,Seventeen ,Eighteen ,Nineteen ,Twenty ');
    SET AMT_Text2   = ' Twenty ,Thirty ,Fourty ,Fifty ,Sixty ,Seventy ,Eighty ,Ninety ';
    SET AMT_Text3   = ' Crore ,Lakh ,Thousand ,Hundred , ';   
    SET Rupee_Txt   = '';
    SET RupeeTxt    = '';
    SET Decimal_Txt = '';
    SET SP_Txt3     = '';
    SET WP              = 1 ;
    SET SP             = 1 ;
    SET Words       = '';
    SET _Rupee      = TRUNCATE(nAmount,0);
    #SET RLEN             = 9-LENGTH(_Rupee);
    #SET Rupee_Txt   = CONCAT(SPACE(RLEN),CONVERT(_Rupee,CHAR)) ;
   
    SET _Decimal    = CAST(SUBSTRING_INDEX(nAmount,'.',-1) AS UNSIGNED);   
    SET PLEN          = 2-LENGTH(_Decimal);
    SET Decimal_Txt = CONCAT(SPACE(PLEN),CONVERT(_Decimal,CHAR));


    WHILE WP < 6 DO
   
      IF SP =  7 THEN
          
           SET RupeeTxt = Rupee_Txt;
               SET SP =SP+1;
          # SET RupeeTxt = CONCAT('0',RupeeTxt);
           SET Words=Number2Char(RupeeTxt,AMT_Text1,AMT_Text2);
                  
       ELSE
                           
		 SET RupeeTxt = Rupee_Txt;
         SET SP =SP+2;
         SET Words=Number2Char(RupeeTxt,AMT_Text1,AMT_Text2);
                                    
       END IF;  
      
       IF Words != '' THEN
     
           IF AMT_Words != '' AND WP = 6 THEN          
               SET AMT_Words =CONCAT(AMT_Words,'and ');       
           END IF;
           
            SET SP_Txt1 = SUBSTRING_INDEX(AMT_Text3,',',WP);
            SET SP_Txt2 = SUBSTRING_INDEX(SP_Txt1,',',WP-1);
            SET SP_Txt3 = SUBSTRING(SP_Txt1,LENGTH(SP_Txt2)+2,LENGTH(SP_Txt1));
           SET AMT_Words = CONCAT(AMT_Words,Words,SP_Txt3) ;
          
       END IF;
      
       SET WP = WP+1;  
           
    END WHILE;

    IF AMT_Words != '' THEN
        SET AMT_Words = CONCAT(AMT_Words,' ');
    END IF;
   
    /*End of Rupee Side*/
   
    SET Words=Number2Char(Decimal_Txt,AMT_Text1,AMT_Text2);
   
    IF Words != '' AND AMT_Words != "" THEN
        SET AMT_Words = CONCAT(TRIM(AMT_Words),' and ', 'Paise ');
    END IF;
   
    IF Words != '' THEN
            SET AMT_Words = CONCAT(AMT_Words,Words);
    END IF;
   
    IF AMT_Words != '' THEN
        SET AMT_Words = CONCAT(TRIM(AMT_Words),' Only. )');
    END IF;

    RETURN AMT_Words;
  
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `Number2Char` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` FUNCTION `Number2Char`(
    `cDigits` VARCHAR(500),
    `cAMT_Text1` VARCHAR(500),
    `cAMT_Text2` VARCHAR(500)) RETURNS varchar(2000) CHARSET utf8
    DETERMINISTIC
BEGIN

DECLARE Words VARCHAR(2000);
DECLARE AMT_Txt1 VARCHAR(2000);
DECLARE AMT_Txt2 VARCHAR(2000);
DECLARE AMT_Txt3 VARCHAR(2000);
DECLARE Digits INT;
DECLARE Value  INT;

SET Words ='';
    IF cDigits > '20' THEN   
  
        SET Digits = CAST(LEFT(cDigits,1) AS UNSIGNED)-1;
       
        SET AMT_Txt1 = SUBSTRING_INDEX(cAMT_Text2,',',Digits);
        SET AMT_Txt2 = SUBSTRING_INDEX(AMT_Txt1,',',Digits-1);   
        SET Words =SUBSTRING(AMT_Txt1,LENGTH(AMT_Txt2)+2,LENGTH(AMT_Txt1));
       
        SET cDigits = CONCAT("0",RIGHT(cDigits,1)) ;
       
    END IF;
   
        SET Digits = CAST(cDigits AS UNSIGNED);
   
        SET AMT_Txt1 = SUBSTRING_INDEX(cAMT_Text1,',',Digits);
        SET AMT_Txt2 = SUBSTRING_INDEX(AMT_Txt1,',',Digits-1);   
        SET AMT_Txt3 = SUBSTRING(AMT_Txt1,LENGTH(AMT_Txt2)+2,LENGTH(AMT_Txt1));
        SET Words =CONCAT(Words,AMT_Txt3);

RETURN Words;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `number_to_string` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` FUNCTION `number_to_string`(n INT) RETURNS varchar(100) CHARSET latin1
BEGIN
        -- This function returns the string representation of a number.
        -- It's just an example... I'll restrict it to hundreds, but
        -- it can be extended easily.
        -- The idea is: 
        --      For each digit you need a position,
        --      For each position, you assign a string
        declare ans varchar(100);
        declare dig1, dig2, dig3,dig4 int; -- (one variable per digit)

        set ans = '';
        set dig4 = floor(n/1000);
        set dig3 = floor(n /100) - dig4*10;
        set dig2 = floor(n / 10) - dig3*10;
        set dig1 = n - (dig4*1000 + dig3*100 + dig2*10);

        if dig4 > 0 then
            case
                when dig4=1 then set ans=concat(ans, 'one Thousand');
                when dig4=2 then set ans=concat(ans, 'two Thousand');
                when dig4=3 then set ans=concat(ans, 'three Thousand');
                when dig4=4 then set ans=concat(ans, 'four Thousand');
                when dig4=5 then set ans=concat(ans, 'five Thousand');
                when dig4=6 then set ans=concat(ans, 'six Thousand');
                when dig4=7 then set ans=concat(ans, 'seven Thousand');
                when dig4=8 then set ans=concat(ans, 'eight Thousand');
                when dig4=9 then set ans=concat(ans, 'nine Thousand');
                else set ans = ans;
            end case;
        end if;

        if dig3 > 0 then
            case
                when dig3=1 then set ans=concat(ans, 'one hundred');
                when dig3=2 then set ans=concat(ans, 'two hundred');
                when dig3=3 then set ans=concat(ans, 'three hundred');
                when dig3=4 then set ans=concat(ans, 'four hundred');
                when dig3=5 then set ans=concat(ans, 'five hundred');
                when dig3=6 then set ans=concat(ans, 'six hundred');
                when dig3=7 then set ans=concat(ans, 'seven hundred');
                when dig3=8 then set ans=concat(ans, 'eight hundred');
                when dig3=9 then set ans=concat(ans, 'nine hundred');
                else set ans = ans;
            end case;
        end if;

        if dig2 = 1 then
            case
                when (dig2*10 + dig1) = 10 then set ans=concat(ans,' ten');
                when (dig2*10 + dig1) = 11 then set ans=concat(ans,' eleven');
                when (dig2*10 + dig1) = 12 then set ans=concat(ans,' twelve');
                when (dig2*10 + dig1) = 13 then set ans=concat(ans,' thirteen');
                when (dig2*10 + dig1) = 14 then set ans=concat(ans,' fourteen');
                when (dig2*10 + dig1) = 15 then set ans=concat(ans,' fifteen');
                when (dig2*10 + dig1) = 16 then set ans=concat(ans,' sixteen');
                when (dig2*10 + dig1) = 17 then set ans=concat(ans,' seventeen');
                when (dig2*10 + dig1) = 18 then set ans=concat(ans,' eighteen');
                when (dig2*10 + dig1) = 19 then set ans=concat(ans,' nineteen');
                else set ans=ans;
            end case;
        else
            if dig2 > 0 then
                case
                    when dig2=2 then set ans=concat(ans, ' twenty');
                    when dig2=3 then set ans=concat(ans, ' thirty');
                    when dig2=4 then set ans=concat(ans, ' fourty');
                    when dig2=5 then set ans=concat(ans, ' fifty');
                    when dig2=6 then set ans=concat(ans, ' sixty');
                    when dig2=7 then set ans=concat(ans, ' seventy');
                    when dig2=8 then set ans=concat(ans, ' eighty');
                    when dig2=9 then set ans=concat(ans, ' ninety');
                    else set ans=ans;
                end case;
            end if;
            if dig1 > 0 then
                case
                    when dig1=1 then set ans=concat(ans, ' one');
                    when dig1=2 then set ans=concat(ans, ' two');
                    when dig1=3 then set ans=concat(ans, ' three');
                    when dig1=4 then set ans=concat(ans, ' four');
                    when dig1=5 then set ans=concat(ans, ' five');
                    when dig1=6 then set ans=concat(ans, ' six');
                    when dig1=7 then set ans=concat(ans, ' seven');
                    when dig1=8 then set ans=concat(ans, ' eight');
                    when dig1=9 then set ans=concat(ans, ' nine');
                    else set ans=ans;
                end case;
            end if;
        end if;

        return trim(ans);
    END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-05-04 23:09:02
