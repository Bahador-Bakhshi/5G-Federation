graph [
  node [
    id 0
    label 1
    disk 6
    cpu 1
    memory 3
  ]
  node [
    id 1
    label 2
    disk 8
    cpu 4
    memory 9
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 2
    memory 14
  ]
  node [
    id 3
    label 4
    disk 2
    cpu 3
    memory 5
  ]
  node [
    id 4
    label 5
    disk 2
    cpu 1
    memory 7
  ]
  node [
    id 5
    label 6
    disk 9
    cpu 2
    memory 13
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 32
    bw 137
  ]
  edge [
    source 0
    target 1
    delay 34
    bw 132
  ]
  edge [
    source 0
    target 2
    delay 26
    bw 90
  ]
  edge [
    source 0
    target 3
    delay 34
    bw 63
  ]
  edge [
    source 1
    target 4
    delay 26
    bw 142
  ]
  edge [
    source 2
    target 4
    delay 35
    bw 158
  ]
  edge [
    source 3
    target 4
    delay 31
    bw 84
  ]
  edge [
    source 4
    target 5
    delay 27
    bw 157
  ]
]
