graph [
  node [
    id 0
    label 1
    disk 7
    cpu 2
    memory 7
  ]
  node [
    id 1
    label 2
    disk 6
    cpu 4
    memory 3
  ]
  node [
    id 2
    label 3
    disk 10
    cpu 4
    memory 4
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
    disk 9
    cpu 4
    memory 5
  ]
  node [
    id 5
    label 6
    disk 6
    cpu 4
    memory 6
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 30
    bw 85
  ]
  edge [
    source 0
    target 1
    delay 27
    bw 176
  ]
  edge [
    source 1
    target 2
    delay 35
    bw 167
  ]
  edge [
    source 1
    target 3
    delay 28
    bw 140
  ]
  edge [
    source 2
    target 4
    delay 25
    bw 128
  ]
  edge [
    source 3
    target 5
    delay 34
    bw 111
  ]
]
