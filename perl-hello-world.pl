use Net::Netconf::Manager;
my $hostname = 'X.X.X.X';
my $login= 'username';
my $pass = 'password';
$jnx = new Net::Netconf::Manager( 'access' => 'ssh',
                'login' => $login,
                'password' => $pass,
                'hostname' => $hostname);
print "Connection established: " . $jnx->get_session_id . "\n";
my $reply=$jnx->get_system_information();
print "Server request: \n $jnx->{'request'}\n Server response: \n $jnx->{'server_response'} \n";
my $config= $jnx->get_dom();
$jnx->disconnect();
