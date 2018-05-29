<?php
/**
 * WordPress基础配置文件。
 *
 * 这个文件被安装程序用于自动生成wp-config.php配置文件，
 * 您可以不使用网站，您需要手动复制这个文件，
 * 并重命名为“wp-config.php”，然后填入相关信息。
 *
 * 本文件包含以下配置选项：
 *
 * * MySQL设置
 * * 密钥
 * * 数据库表名前缀
 * * ABSPATH
 *
 * @link https://codex.wordpress.org/zh-cn:%E7%BC%96%E8%BE%91_wp-config.php
 *
 * @package WordPress
 */

// ** MySQL 设置 - 具体信息来自您正在使用的主机 ** //
/** WordPress数据库的名称 */
define('DB_NAME', 'wordpress');

/** MySQL数据库用户名 */
define('DB_USER', 'root');

/** MySQL数据库密码 */
define('DB_PASSWORD', '');

/** MySQL主机 */
define('DB_HOST', '127.0.0.1');

/** 创建数据表时默认的文字编码 */
define('DB_CHARSET', 'utf8');

/** 数据库整理类型。如不确定请勿更改 */
define('DB_COLLATE', '');

/**#@+
 * 身份认证密钥与盐。
 *
 * 修改为任意独一无二的字串！
 * 或者直接访问{@link https://api.wordpress.org/secret-key/1.1/salt/
 * WordPress.org密钥生成服务}
 * 任何修改都会导致所有cookies失效，所有用户将必须重新登录。
 *
 * @since 2.6.0
 */
define('AUTH_KEY',         'N.$C`z~> ;I*I/85$m;8Zh%<w:7^!*biUI/({p42qjV$n|s3v0=w$`U-|of BnWY');
define('SECURE_AUTH_KEY',  'm5[LE$RE54YAzuQy)BkFk(OY,wt+]q</@4 mM=jcZvm][,4]x,9Pg |jNJlrH19!');
define('LOGGED_IN_KEY',    ';l|NYf:<1}oT!caMO:dRjmQ=eDvfe*G?4Noc.yBP~S~Yj;{g)-S,v,HDkULS=M<}');
define('NONCE_KEY',        '~Xwp/^Q?)52m,UXrOAM/.uTPAeD)yG0_ytLTZ GO(Y?~`hAaApdHUYB8L[6I}N|Z');
define('AUTH_SALT',        ' p}{W:kjHl@XR&Ry#41wRvkJuY8.!kpR!{k_^43h-*AS/nrla7mSciL*XvP:mRSd');
define('SECURE_AUTH_SALT', '4i`b*#P.|9Jy/ORmh]/d2qmH<:O3D<5(jAP0b1Zj$,7W%==]|0kTFRS2xkPN])/X');
define('LOGGED_IN_SALT',   '5Ko:5/7|$g:~L zr0fz^#_?0=B(t &VFzEi -{hQ#/H,OTaR/ppF[9B2.LjR9|Jj');
define('NONCE_SALT',       '{4_H{U^AH*z(mcg))i0klyY#}q!rXh9&=HbHhNO=&9!~uQ]J^@d@TUG=j^2u THV');

/**#@-*/

/**
 * WordPress数据表前缀。
 *
 * 如果您有在同一数据库内安装多个WordPress的需求，请为每个WordPress设置
 * 不同的数据表前缀。前缀名只能为数字、字母加下划线。
 */
$table_prefix  = 'wp_';

/**
 * 开发者专用：WordPress调试模式。
 *
 * 将这个值改为true，WordPress将显示所有用于开发的提示。
 * 强烈建议插件开发者在开发环境中启用WP_DEBUG。
 *
 * 要获取其他能用于调试的信息，请访问Codex。
 *
 * @link https://codex.wordpress.org/Debugging_in_WordPress
 */
define('WP_DEBUG', false);

/**
 * zh_CN本地化设置：启用ICP备案号显示
 *
 * 可在设置→常规中修改。
 * 如需禁用，请移除或注释掉本行。
 */
define('WP_ZH_CN_ICP_NUM', true);

/* 好了！请不要再继续编辑。请保存本文件。使用愉快！ */

/** WordPress目录的绝对路径。 */
if ( !defined('ABSPATH') )
	define('ABSPATH', dirname(__FILE__) . '/');

/** 设置WordPress变量和包含文件。 */
require_once(ABSPATH . 'wp-settings.php');
