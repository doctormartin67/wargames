<?php
$string = "<script>alert('XSS');</script>";
$string = mb_convert_encoding($string, 'UTF-7');
echo $string
?>
