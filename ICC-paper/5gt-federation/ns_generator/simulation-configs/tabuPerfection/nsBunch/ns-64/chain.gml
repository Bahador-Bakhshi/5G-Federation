graph [
  node [
    id 0
    label 1
    disk 6
    cpu 1
    memory 8
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 4
    memory 9
  ]
  node [
    id 2
    label 3
    disk 4
    cpu 3
    memory 7
  ]
  node [
    id 3
    label 4
    disk 5
    cpu 1
    memory 5
  ]
  node [
    id 4
    label 5
    disk 5
    cpu 4
    memory 11
  ]
  node [
    id 5
    label 6
    disk 7
    cpu 1
    memory 10
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 27
    bw 111
  ]
  edge [
    source 0
    target 1
    delay 29
    bw 166
  ]
  edge [
    source 0
    target 2
    delay 25
    bw 119
  ]
  edge [
    source 1
    target 3
    delay 34
    bw 198
  ]
  edge [
    source 2
    target 3
    delay 34
    bw 187
  ]
  edge [
    source 3
    target 4
    delay 26
    bw 58
  ]
  edge [
    source 4
    target 5
    delay 31
    bw 119
  ]
]
