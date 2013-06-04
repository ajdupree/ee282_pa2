#!/usr/bin/perl

opendir my($dir), "../q4/data" or die "Could not open ../q4/data";
my @dirs  = readdir $dir;
close $dir;

# dont want . and .. in the directory listing
shift @dirs;
shift @dirs;

my @results;

foreach $dir (@dirs) {
  my($time, $energy, $edp, $area);
  if($dir =~ /art_(wide|narrow)_([0-9]+)_[0-9]+_([0-9]+)_L1_([0-9]+)_([0-9]+)_L2_([0-9]+)_([0-9]+)_L3_([0-9]+)_([0-9]+)(_MEMBW_([0-9]+))?/) {
    my($width, $cores, $freq, $l1size, $l1assoc, $l2size, $l2assoc, $l3size, $l3assoc) = ($1,$2,$3,$4,$5,$6,$7,$8,$9);
    next if $l2size > 512;
    if(open STATS, "<../q4/data/$dir/stats.txt") { 
      while(<STATS>) {
        if(/Time \(s\).*: ([0-9]*\.[0-9]*)/) {
          $time = $1;  
        } elsif(/Total energy \(J\).*: ([0-9]*\.[0-9]*)/) {
          $energy = $1;
        } elsif(/Energy-Delay Product.*: ([0-9]*\.[0-9]*)/) {
          $edp= $1;
        } elsif(/Area.*: ([0-9]*\.?[0-9]*)/) {
          $area= $1;
        }
      }
      push @results, {'time'=>$time,'energy'=>$energy,'edp'=>$edp,'width'=>$width,'cores'=>$cores,'freq'=>$freq,'l1size'=>$l1size,'l1assoc'=>$l1assoc, 
                      'l2size'=>$l2size,'l2assoc'=>$l2assoc,'l3size'=>$l3size,'l3assoc'=>$l3assoc,'dir'=>$dir,'area'=>$area};
      close STATS;
    } else {
      print "ERROR: couldn't open ../q4/data/$dir/stats.txt\n"; 
    }
  } else {
    die "$_ did not match the regexp\n";
  }
}

print "Time (S):\ntime,test\n";
foreach $i (1..$#results) {
  print $results[$i]{'time'}.",".$results[$i]{'dir'}."\n";
}

print "\n\nEnergy (J):\ntime,test\n";
foreach $i (1..$#results) {
  print $results[$i]{'energy'}.",".$results[$i]{'dir'}."\n";
}

print "Performance/Area:\ntime,test";
foreach $i (1..$#results) {
  print 1/($results[$i]{'area'}*$results[$i]{'time'}).",".$results[$i]{'dir'}."\n";
}

print "Performance/Energy:\ntime,test";
foreach $i (1..$#results) {
  print 1/($results[$i]{'energy'}*$results[$i]{'time'}).",".$results[$i]{'dir'}."\n";
}
