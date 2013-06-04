#!usr/bin/perl

my $path = "../q2/art_wide_8_8_1700_L1_32_4_L2_512_8_L3_8192_16_MEMBW_";

my %times;
my %energies;
my %energy_delay_product;

for(my $bw = 1000; $bw <= 10000; $bw += 200)
{
  if(!open STATS, "<${path}${bw}/stats.txt")
  {
    print "could not open ${path}${bw}/stats.txt\n";
  }
  else
  {
    while(<STATS>)
    {
      if(/Time \(s\).*: ([0-9]*\.[0-9]*)/)
      {
        $times{$bw} = $1;  
      }
      if(/Total energy \(J\).*: ([0-9]*\.[0-9]*)/)
      {
        $energies{$bw} = $1;
      }
      if(/Energy-Delay Product.*: ([0-9]*\.[0-9]*)/)
      {
        $energy_delay_product{$bw} = $1;
      }
    }
  close STATS;
  }
}

print "Time\n";
while((my $bw, my $time) = each %times)
{
  print "$bw,$time\n";
}

print "\nEnergy\n";
while((my $bw, my $energy) = each %energies)
{
  print "$bw,$energy\n";
}

print "\nEnergy-Delay Product\n";
while((my $bw, my $edp) = each %energy_delay_product)
{
  print "$bw,$edp\n";
}
