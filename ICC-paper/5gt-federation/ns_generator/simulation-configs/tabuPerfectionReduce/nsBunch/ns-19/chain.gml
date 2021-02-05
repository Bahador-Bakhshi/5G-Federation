graph [
  node [
    id 0
    label 1
    disk 5
    cpu 3
    memory 12
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 4
    memory 14
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 4
    memory 11
  ]
  node [
    id 3
    label 4
    disk 6
    cpu 2
    memory 11
  ]
  node [
    id 4
    label 5
    disk 10
    cpu 3
    memory 13
  ]
  node [
    id 5
    label 6
    disk 3
    cpu 4
    memory 16
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 31
    bw 132
  ]
  edge [
    source 0
    target 1
    delay 26
    bw 82
  ]
  edge [
    source 0
    target 2
    delay 26
    bw 130
  ]
  edge [
    source 0
    target 3
    delay 31
    bw 150
  ]
  edge [
    source 2
    target 4
    delay 33
    bw 100
  ]
  edge [
    source 3
    target 5
    delay 34
    bw 111
  ]
]
