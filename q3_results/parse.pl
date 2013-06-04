#!usr/bin/perl

my %l2size = 
(
  'wide1' => 32768,  
  'wide2' => 16384,  
  'wide3' => 16384,  
  'wide4' => 8192,  
  'wide5' => 4096,
  'wide6' => 2048,  
  'wide7' => 1024,  
  'wide8' => 512,  
  
  'narrow1' => 32768,  
  'narrow2' => 32768,  
  'narrow3' => 16384,  
  'narrow4' => 16384,  
  'narrow5' => 8192,  
  'narrow6' => 8192,  
  'narrow7' => 8192,  
  'narrow8' => 4096,  
  'narrow9' => 4096,  
  'narrow10' => 4096,  
  'narrow11' => 2048,  
  'narrow12' => 2048,  
  'narrow13' => 2048,  
  'narrow14' => 2048,  
  'narrow15' => 1024,  
  'narrow16' => 1024,  
);

sub get_test_path
{
  my($width, $cores) = @_;
  return "../q3/data/blackscholes_${width}_${cores}_${cores}_1700_L1_32_4_L2_".$l2size{$width.$cores}."_8_L3_8192_16_MEMBW_6400/stats.txt";
}

my @wide_times;
my @wide_energies;
my @narrow_times;
my @narrow_energies;


foreach my $cores (1..8)
{
  if(!open STATS, "<" . &get_test_path("wide",$cores))
  {
    print "could not open " . &get_test_path("wide",$cores) . "\n";
  }
  else
  {
    while(<STATS>)
    {
      if(/Time \(s\).*: ([0-9]*\.[0-9]*)/)
      {
        $wide_times[$cores] = $1;  
      }
      if(/Total energy \(J\).*: ([0-9]*\.[0-9]*)/)
      {              
        $wide_energies[$cores] = $1;
      }
    }
  close STATS;
  }
}

foreach my $cores (1..16)
{
  if(!open STATS, "<" . &get_test_path("narrow",$cores))
  {
    print "could not open " . &get_test_path("narrow",$cores) . "\n";
  }
  else
  {
    while(<STATS>)
    {
      if(/Time \(s\).*: ([0-9]*\.[0-9]*)/)
      {
        $narrow_times[$cores] = $1;  
      }
      if(/Total energy \(J\).*: ([0-9]*\.[0-9]*)/)
      {
        $narrow_energies[$cores] = $1;
      }
    }
  close STATS;
  }
}


print "Time\ncores,narrow,wide\n";
foreach my $cores (1..16)
{
  print "$cores,";
  if(defined($narrow_times[$cores])) {
    print "$narrow_times[$cores]";
  } else {
    print "";
  }
  if(defined($wide_times[$cores])) {
    print ",$wide_times[$cores]\n";
  } else {
    print "\n";
  }
}

print "\nEnergy\ncores,narrow,wide\n";
foreach my $cores (1..16)
{
  print "$cores,";
  if(defined($narrow_energies[$cores])) {
    print "$narrow_energies[$cores]";
  } else {
    print "";
  }
  if(defined($wide_energies[$cores])) {
    print ",$wide_energies[$cores]\n";
  } else {
    print "\n";
  }
}
