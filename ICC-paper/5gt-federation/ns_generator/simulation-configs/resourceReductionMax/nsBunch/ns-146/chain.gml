graph [
  node [
    id 0
    label 1
    disk 9
    cpu 4
    memory 8
  ]
  node [
    id 1
    label 2
    disk 8
    cpu 2
    memory 16
  ]
  node [
    id 2
    label 3
    disk 4
    cpu 4
    memory 4
  ]
  node [
    id 3
    label 4
    disk 1
    cpu 4
    memory 14
  ]
  node [
    id 4
    label 5
    disk 3
    cpu 2
    memory 11
  ]
  node [
    id 5
    label 6
    disk 1
    cpu 2
    memory 11
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 32
    bw 162
  ]
  edge [
    source 0
    target 1
    delay 33
    bw 103
  ]
  edge [
    source 1
    target 2
    delay 28
    bw 126
  ]
  edge [
    source 2
    target 3
    delay 29
    bw 65
  ]
  edge [
    source 2
    target 4
    delay 27
    bw 96
  ]
  edge [
    source 3
    target 5
    delay 27
    bw 95
  ]
  edge [
    source 4
    target 5
    delay 31
    bw 97
  ]
]
