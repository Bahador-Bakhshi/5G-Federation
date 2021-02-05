graph [
  node [
    id 0
    label 1
    disk 10
    cpu 4
    memory 13
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 4
    memory 9
  ]
  node [
    id 2
    label 3
    disk 7
    cpu 2
    memory 3
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 1
    memory 5
  ]
  node [
    id 4
    label 5
    disk 7
    cpu 3
    memory 3
  ]
  node [
    id 5
    label 6
    disk 10
    cpu 1
    memory 2
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 26
    bw 198
  ]
  edge [
    source 0
    target 1
    delay 34
    bw 81
  ]
  edge [
    source 1
    target 2
    delay 25
    bw 87
  ]
  edge [
    source 2
    target 3
    delay 26
    bw 84
  ]
  edge [
    source 2
    target 4
    delay 31
    bw 90
  ]
  edge [
    source 2
    target 5
    delay 30
    bw 187
  ]
]
