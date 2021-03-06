graph [
  node [
    id 0
    label 1
    disk 5
    cpu 1
    memory 8
  ]
  node [
    id 1
    label 2
    disk 6
    cpu 1
    memory 11
  ]
  node [
    id 2
    label 3
    disk 7
    cpu 3
    memory 8
  ]
  node [
    id 3
    label 4
    disk 6
    cpu 4
    memory 14
  ]
  node [
    id 4
    label 5
    disk 3
    cpu 3
    memory 4
  ]
  node [
    id 5
    label 6
    disk 10
    cpu 1
    memory 16
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 26
    bw 83
  ]
  edge [
    source 0
    target 1
    delay 32
    bw 74
  ]
  edge [
    source 0
    target 2
    delay 31
    bw 69
  ]
  edge [
    source 1
    target 3
    delay 26
    bw 107
  ]
  edge [
    source 2
    target 3
    delay 35
    bw 63
  ]
  edge [
    source 3
    target 4
    delay 26
    bw 174
  ]
  edge [
    source 4
    target 5
    delay 27
    bw 81
  ]
]
