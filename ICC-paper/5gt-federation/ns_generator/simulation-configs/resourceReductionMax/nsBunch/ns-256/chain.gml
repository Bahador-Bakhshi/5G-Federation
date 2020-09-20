graph [
  node [
    id 0
    label 1
    disk 10
    cpu 2
    memory 4
  ]
  node [
    id 1
    label 2
    disk 4
    cpu 1
    memory 7
  ]
  node [
    id 2
    label 3
    disk 3
    cpu 2
    memory 14
  ]
  node [
    id 3
    label 4
    disk 3
    cpu 3
    memory 3
  ]
  node [
    id 4
    label 5
    disk 9
    cpu 3
    memory 16
  ]
  node [
    id 5
    label 6
    disk 2
    cpu 2
    memory 10
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 35
    bw 145
  ]
  edge [
    source 0
    target 1
    delay 31
    bw 65
  ]
  edge [
    source 0
    target 2
    delay 31
    bw 85
  ]
  edge [
    source 1
    target 3
    delay 27
    bw 93
  ]
  edge [
    source 2
    target 3
    delay 27
    bw 188
  ]
  edge [
    source 3
    target 4
    delay 27
    bw 200
  ]
  edge [
    source 4
    target 5
    delay 34
    bw 150
  ]
]
