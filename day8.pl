#!/usr/bin/env perl

# This perl script creates a string that it then passes to python to evaluate
# Is this at all practical? Nope :)
use strict;
use warnings;

use File::Slurp;

my @lines = read_file('input.txt');
my $out_top = "regs = []\nbiggest = 0\n";
my $out_mid = '';
my $out_bottom = '';
my $out_footer = "print('Part One:', max(regs), '\\nPart Two:', biggest)";

foreach my $line (@lines) {
  # initialize registers
  if ($line =~ /(^[^\s]+)\s/) {
    $out_top .= "$1 = 0\n";
    $out_bottom .= "regs.append($1)\n";
  }

  # replace inc/dec
  $line =~ s/ inc / += /;
  $line =~ s/ dec / -= /;

  if ($line =~ /(([^\s]+)\s[^\s]+\s[^\s]+)\s([^\n]+)/) {
    $out_mid .= "$3:\n    $1\n    biggest = max($2, biggest)\n"
  }
}

my $result = `python3 -c "$out_top\n$out_mid\n$out_bottom\n$out_footer"`;
print $result;
