graph [
  node [
    id 0
    label 1
    disk 2
    cpu 2
    memory 15
  ]
  node [
    id 1
    label 2
    disk 6
    cpu 2
    memory 10
  ]
  node [
    id 2
    label 3
    disk 1
    cpu 3
    memory 13
  ]
  node [
    id 3
    label 4
    disk 2
    cpu 4
    memory 11
  ]
  node [
    id 4
    label 5
    disk 5
    cpu 3
    memory 16
  ]
  node [
    id 5
    label 6
    disk 7
    cpu 2
    memory 5
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 28
    bw 111
  ]
  edge [
    source 0
    target 1
    delay 25
    bw 126
  ]
  edge [
    source 1
    target 2
    delay 35
    bw 54
  ]
  edge [
    source 2
    target 3
    delay 31
    bw 103
  ]
  edge [
    source 2
    target 4
    delay 30
    bw 152
  ]
  edge [
    source 2
    target 5
    delay 33
    bw 79
  ]
]
