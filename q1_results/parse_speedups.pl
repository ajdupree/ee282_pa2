#!usr/bin/perl

my @tests = qw(art blackscholes fluidanimate streamcluster swaptions);

sub get_test_path
{
  my($test, $cores) = @_;
  return "../q1/${test}_wide_${cores}_${cores}_1700_L1_32_4_L2_512_8_L3_8192_16/stats.txt";
}

foreach $test (@tests)
{
  my @times;
  my @energies;
  my @speedups;
  foreach $cores (1..8)
  {
    if(!open STATS, "<" . &get_test_path($test,$cores))
    {
      print "could not open " . &get_test_path($test,$cores) . "\n";
    }
    else
    {
      while(<STATS>)
      {
        if(/Time \(s\).*: ([0-9]*\.[0-9]*)/)
        {
          $times[$cores] = $1;  
        }
        elsif(/Total energy \(J\).*: ([0-9]*\.[0-9]*)/)
        {
          $energies[$cores] = $1;  
        }
      }
    close STATS;
    }
  }
  print "$test\ncores,speedup\n";
  foreach $cores (1..$#times)
  { 
    if(defined($times[$cores]))
    {
      my $speedup = $times[1] / $times[$cores];
      print "$cores,$speedup\n";
    }
  }
  print "$test\ncores,energy\n";
  foreach $cores (1..$#energies)
  { 
    if(defined($energies[$cores]))
    {
      print "$cores,$energies[$cores]\n";
    }
  }
  print "$test\ncores,Ave Power\n";
  foreach $cores (1..$#energies)
  { 
    if(defined($energies[$cores]) && defined($times[$cores]))
    {
      my $power = $energies[$cores] / $times[$cores];
      print "$cores,$power\n";
    }
  }
  print "\n";
} 
