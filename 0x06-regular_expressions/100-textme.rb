#!/usr/bin/env ruby

senderPattern = /\[from:(\+?[\w]+)\]/
receiverPattern = /\[to:(\+?[0-9]+)\]/
flagsPattern = /\[flags:([012\-:]*)\]/

senders = ARGV[0].scan(senderPattern).flatten
receivers = ARGV[0].scan(receiverPattern).flatten
flags = ARGV[0].scan(flagsPattern).flatten

dataArray = senders.zip(receivers, flags)

dataArray.each do |sender, receiver, flag|
  puts "#{sender},#{receiver},#{flag}"
end
